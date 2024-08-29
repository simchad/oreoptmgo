"""
jobs.processing
~~~~~~~~~~~~~~~

This module contains numbers of functions for pre-processing
"""
# --------------------------------------
# vscode 터미널에서 pip 안될때
# 원인: python 옳게 설치했더라도 윈도우 클래스에서 pip 위치를 알지 못하기에 발생.
# python3 부터는 pip 내장이므로 python.exe 디렉터리 연결하면 됨.
# C:\Users\Simon\AppData\Local\Programs\Python\Python39\Scipts 를 다음에 추가하면됨.
# (고급 시스템 설정 보기) - (환경변수 탭) - (사용자에 대한 사용자 변수 및 시스템 변수의 path에 추가)
# --------------------------------------
# 주피터 노트북에 익숙해지지 말고 파이썬 커널에 익숙해 져야해.
# --------------------------------------

# Load packages
from api_request import uniprot_requests
import csv
import os
import pandas as pd
import re
from time import localtime, strftime


class DB_request_tools:
    # processing.py - DB_request class 로 관리할 것들은 ???
    def __init__(self, df):
        self.df = df
    

    # Uniprot DB request & respond
    def uniprot_request(self, AC_ID):
        # import uniprot_requests as uniprot_request
        Prot_ids = pd.Series(self.df[AC_ID])
        #Prot_ids = ('A0FGR8', 'Q99613', 'O00148')
        #Prot_ids = ('A6NHR9', 'E9PAV3', 'O00151')

        link = uniprot_requests.execute(Prot_ids)
        # %2C[attribute]
        tsv_rst = uniprot_requests.get_id_mapping_results_stream(str(link)+'?compressed=true&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Clength%2Csequence&format=tsv')
        reader = csv.DictReader(tsv_rst, delimiter="\t", quotechar='"')
        df_sub = pd.DataFrame(list(reader))

        # 별일 없으면 순서는 같다. 단, indicies 일치해야.
        self.df['Protein names'] = df_sub['Protein names']
        self.df['Gene names'] = df_sub['Gene Names']
        self.df['Sequence length'] = df_sub['Length']
        return self.df


    # DAVID DB request & respond
    def DAVID_request(self):
        pass


    # KEGG DB request & respond
    def KEGG_request(self):
        pass


    # Reactome request & respond
    def Reactome_request(self):
        pass


class process_base_tools:
    # The tools for base-processing (drop column, split ';')
    def __init__(self, df, target):
        self.df = df
        self.target = target


    # Fnc 'isDrop' drops key == value items in **kwargs
    def isDrop(self, **kwargs):
        for key, value in kwargs.items():
            tmp1 = len(self.df)
            tmp2 = len(self.df[self.df[key] == value])
            ratio = (100*tmp2)/tmp1
            
            # key에 해당하는 value를 가진 entry 드랍.
            self.df.drop(self.df[self.df[key] == value].index, inplace=True)
            
            # value가 숫자인 경우: column 드랍하지 않음.
            # e.g., Razor + unique peptides의 경우, value = 1 인 entry 드랍 하지만, 나머지 entry는 남아야하므로.
            if isinstance(value, str):
                self.df.drop(columns=[key], inplace=True)
                print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped, [' %ratio +key+'] column removed.')
            else:
                print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped. ['%ratio +key+' = '+str(value)+']')
                # print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped, ['+key+'] column removed' %ratio) <- 이 구문은 동작안함. %~~ 이게 string으로 나눈 같은 구역에 있어햐 함.
        
        # complete column drop
        print('message! >>> '+str(len(self.df))+' entries left.')
        return self.df


    # Split할 column 이름을 tuple (c1, c2)로 주고, delimiter의 기본값은 세미콜론(;)으로 되어있다.
    def split_items(self, *args):
        for arg in args:
            tmp_series = pd.Series(self.df[arg])
            for ele in tmp_series:
                tmp = ele.split(';')[0]
                tmp_series.replace(ele, tmp, inplace=True)
            print('message! >>> ['+arg+'] elements were splitted')
        return self.df
    

    # This fnc to find Reporter intensity with 'corrected' or 'count' to eliminated
    def det_corrected_or_count(self):
        reporter = []
        reporter_drop =[]
        cols = pd.Index(self.df.columns).tolist()
        for col in cols:
            if re.search('Reporter', col):
                reporter.append(col)
        for repo in reporter:
            if re.search(('corrected|count'), repo):
                reporter_drop.append(repo)
        reporter = sorted(list(set(reporter) - set(reporter_drop)))
        # return (reporter, reporter_drop)
        return reporter
    

    # This fnc return base columns to create base file with 'Score' column.
    def base_cols(self, cols, reporters):
        if self.target == 'proteinGroups':
            score = cols.index('Score') + 1
            base_columns = cols[:score] + reporters + cols[score:]
        return base_columns
    

    # Different method for creating base csv file.
    def create_base_df(self, cols):
        if self.target == 'proteinGroups':
            self.df = self.df[cols].copy()
        elif self.target == 'peptides':
            self.df = self.df.drop(columns=cols)
        else:
            raise ValueError
        return self.df
    

    # Creating csv file after 'create_base_df' fnc., the file saved under the name 'filename_base_yyyymmdd-hhmmss'
    def create_csv(self):
        ntm = strftime('%Y%m%d-%H%M%S', localtime())
        cwd = os.getcwd()
        filepath ='./output/'+self.target+'_base_'+ntm+'.csv'
        self.df.to_csv(path_or_buf=filepath, sep=',', index=False, encoding='utf-8')
        temp = filepath.replace('/', '\\')
        saved_path = cwd.replace('jobs','')+temp[1:]
        print('message! >>> file created... '+saved_path)
        return saved_path


class process_base:
    # The base-processing of each *.txt files.
    # For Global files.
    def __init__(self, txtpath):
        self.txtpath = txtpath


    def proteinGroups_base(self):
        target = 'proteinGroups'
        filepath = self.txtpath+target+'.txt'
        self.df = pd.read_table(filepath_or_buffer=filepath, index_col=False)
        base_filter = {'Potential contaminant':'+', 'Reverse':'+', 'Only identified by site':'+', 'Razor + unique peptides':1}
        split_cols = ('Protein IDs', 'Best MS/MS')
        rest_cols = [
            'Protein IDs', 'Protein names', 'Gene names', 'Razor + unique peptides',
            'Unique sequence coverage [%]', 'Mol. weight [kDa]','Sequence length',
            'Q-value', 'Score', 'Intensity', 'id', 'Peptide IDs', 'Evidence IDs',
            'Best MS/MS'
        ]
        
        # Drop and split(;) on upper columns
        t = process_base_tools(self.df, target)
        self.df = t.isDrop(**base_filter) 
        self.df = t.split_items(*split_cols)
        self.df.reset_index(drop=True, inplace=True)
                
        # Request protein/gene names to Uniprot-API (1/2)
        r = DB_request_tools(self.df)
        pg_names = r.uniprot_request('Protein IDs')
        
        # Replace protein/gene names from response_DB (2/2)
        self.df['Protein names'] = pg_names['Protein names']
        self.df['Gene names'] = pg_names['Gene names']
        
        # Return reporter intensity cols and merge with rest_cols
        reporter_cols = t.det_corrected_or_count()
        rest = t.base_cols(rest_cols, reporter_cols)
        
        # proteinGroups.txt --> ProteinGroups_base.csv
        self.df = t.create_base_df(rest)
        savepath = t.create_csv()
        return savepath
    

    def peptides_base(self):
        target = 'peptides'
        filepath = self.txtpath+target+'.txt'
        self.df = pd.read_table(filepath_or_buffer=filepath, index_col=False)
        base_filter = {'Reverse':'+', 'Potential contaminant':'+'}
        drop_cols = [
            'N-term cleavage window', 'C-term cleavage window', 'Amino acid before', 'First amino acid', 'Second amino acid',
            'Second last amino acid', 'Last amino acid', 'Amino acid after', 'A Count', 'R Count', 'N Count', 'D Count', 'C Count',
            'Q Count', 'E Count', 'G Count', 'H Count', 'I Count', 'L Count', 'K Count', 'M Count','F Count', 'P Count', 'S Count',
            'T Count', 'W Count', 'Y Count', 'V Count', 'U Count', 'O Count', 'Length', 'Mass', 'Proteins', 'End position',
            'Unique (Groups)', 'Unique (Proteins)'
        ]
        # Drop a number of columns
        t = process_base_tools(self.df, target)
        self.df = t.isDrop(**base_filter)
        self.df.reset_index(drop=True, inplace=True)

        # UNIPROT-API request후 밀리는 현상
        # peptides의 경우, 단백질 1개에서 펩타이드 여러개 detect 되기 때문에 enrich 돼서. 굳이 mapping 할 이유가?
        # Uniprot ID Mapping Job Submission Note 참조.
        # : Please do verify that your list does not contain any duplicates,
        # : and try to split it into smaller chunks in case of problems
        
        # peptides.txt --> peptides_base.csv
        self.df = t.create_base_df(drop_cols)
        savepath = t.create_csv()
        return savepath
    

    def evidence_base(self):
        target = 'evidence'
        filepath = self.txtpath+target+'.txt'
        self.df = pd.read_table(filepath_or_buffer=filepath, index_col=False)
        base_filter = {'Reverse':'+', 'Potential contaminant':'+', 'Type':'MSMS'}
        # Drop a number of columns
        t = process_base_tools(self.df, target)
        self.df = t.isDrop(**base_filter)
        # evidence.txt --> evidence.csv
        savepath = t.create_csv()
        return savepath


if __name__ == "__main__":
    pass

# To do list (Note)
#
# - __name__ == "__main__" 에서 raw file path를 폴더까지 지정후 *_base 함수에 경로를 인수로 주도록.
# - create_csv 를 보편적으로 만들기. path를 따로 받아서 다른 txt에도 사용할 수 있게
# 
# 메모리를 적게 쓰려면: 최종적으로 남길 열을 제외하곤 처음부터 드랍 해놔야함.  
# pd.read_table(usecols=[column names]) : []에 지정한 column만 들고 올 수 있어서 좋음. but, reverse, contam 필터하려면 drop 메서드가 나을 듯.
# TMT, fraction, replication 하게 되면: 다 가져와서 일부 drop이 쉬움.
#
# Build
# 2023.01.21. 22:16, evidence, peptides, proteinGroups_base build for Global set
# 2023.01.26. TMT set available
# Ongoing...
