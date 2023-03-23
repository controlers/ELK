#!/usr/bin/python
# -*- codinig: UTF-8 -*-
import os
import jinja2
#定义模板函数，这个必须有，没有模板函数是无法实现替换的
def render(tpl_path,**kwargs):
    path,filename=os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)

def test_simple():
    iface="ens33"
    cluster_cidr="172.30.0.0/16"
    result=render('/rubbish/kube-flannel.yml.template.j2',**locals())
    print(result)
if __name__ == '__main__':
    test_simple() 
