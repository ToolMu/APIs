import yaml

from parsers import Parser


class YamlParsers(Parser):
    def parser(self, file_path):
        with open(file_path, 'r') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        
        return content


if __name__ == "__main__":
    from utils.constant import BASEDIR
    
    file_path = BASEDIR + '/conf/httporg.yaml'
    print(YamlParsers().parser(file_path))
