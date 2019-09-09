import requests
import re
import pymysql

class NoteSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.proxies = {'http':'http://127.0.0.1:8888'}
        self.auth = ('tarenacode','code_2013')
        self.db = pymysql.connect(
            'localhost',
            'root',
            '123456',
            'stock',
            charset='utf8')
        self.cursor = self.db.cursor()

    # 获取+解析
    def get_parse_page(self):
        res = requests.get(
            url=self.url,
            auth=self.auth,
            headers=self.headers
        )
        res.encoding = 'utf-8'
        html = res.text
        # 解析
        p = re.compile('<a href=.*?>(.*?)/</a>',re.S)
        r_list = p.findall(html)
        # r_list : ['..','AIDCode','ACCCode']
        self.write_mongo(r_list)

    # 保存数据
    def write_mongo(self,r_list):
        ins = 'insert into note values(%s)'
        for r in r_list:
            if r != '..':
                self.cursor.execute(ins,[r])
                self.db.commit()

    def create_table(self):
        with open('code.txt', 'rt') as file:
            data = file.readlines()
            for tbname in data:
                tbname = tbname.replace('\n', '')
                sql_novel = """create table {}(
                    id int primary key auto_increment,
                    code char(8) not null,
                    novel_url varchar(355) not null,
                    cover_url varchar(355) not null
                    )ENGINE=InnoDB DEFAULT CHARSET=utf8;""".format(tbname)

                self.cursor.execute(sql_novel)
                print('%s创建成功！' % tbname)

if __name__ == '__main__':
    spider = NoteSpider()
    # spider.get_parse_page()
    spider.create_table()
