from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open

from markdown import Markdown
import json
from jinja2 import Template

import re

# Create a new reader class, inheriting from the pelican.reader.BaseReader
class NewReader(BaseReader):
    enabled = True  # Yeah, you probably want that :-)

    # The list of file extensions you want this reader to match with.
    # If multiple readers were to use the same extension, the latest will
    # win (so the one you're defining here, most probably).
    file_extensions = ['rad']

    # You need to have a read method, which takes a filename and returns
    # some content and the associated metadata.
    def read(self, filename):

        # template_path = self.settings['YEAH_TEMPLATES'][0]
        metadata = {'template':'cool_article'}

        content = ""
        dictionary = {}
        with open(filename, 'r') as stream:
            dictionary = json.load(stream)
        
        metadata.update(dictionary)
        
        _md = Markdown()

        parsed = {}
        for key, value in metadata.items():
            if key == "cool_description":
                contents = value[2:]#.replace("\n#","\n##")
                contents = "\n" + contents

                if "\n# " in contents:
                    contents = contents.replace("\n#","\n##")

                md_contents = _md.convert(contents)
                md_contents = re.sub(re.compile(r'<img.*?/>'), '', md_contents)

                parsed[key] = md_contents
            elif key == "cool_reviews":

                all_reviews = []
                for ix, v in enumerate(value):

                    unproc_v = v[2:]
                    unproc_v = unproc_v.split("\n")

                    if len(unproc_v[0]) < 3:
                        unproc_v.pop(0)

                    # unproc_v[0] = unproc_v[0].replace("#","")
                    unproc_v[0] = metadata['cool_products'][ix]['title']
                    unproc_v[0] = "\n### " +str(ix+1) + ". " + unproc_v[0] + "\n"

                    # unproc_v[1:] = ["" if "#" in s else  s + "\n\n" for s in unproc_v[1:]]

                    rev_str = []
                    for s in unproc_v[1:]:
                        
                        if ". " in s:
                            s_split = s.split(". ")
                            # print("----", s_split)
                            # s_split = [sp if len(sp)>3 else "" for sp in s_split]
                            s_split = [x for x in s_split if x != '' and x != ' ']
                            s_split = [x if x[-1]=="!" or x[-1]=="?" or x[-1]=="." or x[-1]==":" else x+"." for x in s_split]
                            
                            s = ''.join([sp if len(sp) < 100 else sp+"\n\n" for sp in s_split])
                        if "#" in s:
                            s = re.sub(re.compile(r"[#]+\w+"), '', s)
                            s_split = s.split("\n")
                            s_split = ["" if ("# " in sp or "- " in sp) else sp for sp in s_split]
                            s = ''.join([sp for sp in s_split])


                        rev_str.append(s + "\n\n")

                    unproc_v[1:] = rev_str

                    # print("-----", unproc_v)


                    

                    proc_v =  ''.join(unproc_v[1:]).split("<", 1)[0]

                    rev_text = _md.convert(proc_v)
                    rev_text = rev_text.replace("<pre><code>", "<br>").replace("</code></pre>", "<br>")
                    rev_text = rev_text.replace("<strong>", "").replace("</strong>", "")
                    rev_text = re.sub(re.compile(r'<img.*?/>'), '', rev_text)

                    rev = {}
                    rev["text"] = rev_text
                    rev["title"] = metadata['cool_products'][ix]['title']
                    try:
                        rev["image_l"] = metadata['cool_products'][ix]['image_l']
                    except:
                        pass
                    rev["clickurl"] = metadata['cool_products'][ix]['clickurl']

                    all_reviews.append(rev)


                parsed[key] = all_reviews
            else:
                parsed[key] = self.process_metadata(key, value)
            # print(key)

        # parsed["cool_description"] = Markdown().convert(parsed["cool_description"])

        tt =  parsed["title_plural"] if "title_plural" in parsed else parsed["title"]

        parsed["metadescription"] = "Explore {} for 2023. Our detailed reviews provide the insights you need for an informed purchase.".format(tt.lower())

        if "title_plural" in parsed:
            parsed["keywords"] = parsed["title_plural"].replace('The 10 Best ', '')
        else:
            parsed["keywords"] = parsed["title"].replace('The 10 Best ', '')

        return content, parsed



def add_reader(readers):
    readers.reader_classes['rad'] = NewReader

# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)