import requests,json,sys,os
class GetComment:
    def __init__(self,shortcode):
        self.header = {}
        self.header['Host']= "www.instagram.com"
        self.header['User-Agent'] ="Mozilla/5.0 "\
                                    "(Linux; Android 8.0.0; SM-G960F Build/R16NW)"\
                                    " AppleWebKit/537.36 (KHTML, like Gecko)"\
                                    " Chrome/62.0.3202.84 Mobile Safari/537.36"
        self.header["Accept"] = "*/*"
        self.header["Accept-Language"] ="en-US,en;q=0.5"
        self.header["Accept-Encoding"] = "gzip, deflate, br"
        self.header["X-IG-WWW-Claim"] = "0"
        self.header["X-Requested-With"] = "XMLHttpRequest"
        
        session = requests.Session()
        response = session.get("https://www.instagram.com/p/"+shortcode+"/")
        self.header["Cookie"] = "ig_did=911EA619-8E3C-47E4-9260-8BE2BCE35809;"\
                                " csrftoken=TozTWtlvntuBXFc6U2Nu9wUNFBW6ZcJk;"\
                                "rur=FRC; mid=XeTm6gAEAAEUkRvudCIyMLEO49Mx;"\
                                "urlgen=\"{\\\"95.2.8.27\\\":"\
                                " 9121}:1ibjTF:GkygUV4iTzSCjR-jiUATInQxSys\""
        if(bool(session.cookies.get_dict())):
            self.header["Cookie"] = str(session.cookies.get_dict())[1:-1]
        print(self.header['Cookie'])
        self.header["DNT"] = "1"
        self.header["Connection"] = "keep-alive"
        self.query_hash = "97b41c52301f77ce508f55e66d17620e"
        self.shortcode = shortcode #input("ShortCode: ")
        self.url = "https://www.instagram.com/graphql/query/?query_hash=" + self.query_hash
        self.variables = "&variables={\"shortcode\":\"" + self.shortcode +"\",\"first\":13,\"after\":\""

        self.hasNextPage = True
        self.end_cursor = ""
    def getComments(self):
        if(not self.hasNextPage or self.shortcode==""):
            return None
        try:
            response = requests.get(self.url + self.variables + self.end_cursor + "\"}",headers=self.header ) 
            resp = json.loads(response.text)
            page_info = resp["data"]["shortcode_media"]["edge_media_to_parent_comment"]["page_info"]
            edges = resp["data"]["shortcode_media"]["edge_media_to_parent_comment"]["edges"]
            self.hasNextPage = page_info["has_next_page"]
            self.end_cursor = page_info["end_cursor"]
        except Exception as e:
            resp = json.loads(response.text)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            raise Exception(str(resp['message']))
        return edges
    #for edge in edges:
        #	print(edge["node"]["text"])
