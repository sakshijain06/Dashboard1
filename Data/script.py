import urllib
from django.utils import timezone
import urllib2
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser
from Data.models import TestCase
import new
from django.http.response import HttpResponse


class testcaseInfo:
    pass

def fetchTestCaseInfoAndPersist(request):
    global ATSVersionNum
    global ASVersionNum
    global client
    global testCaseInfoLst
    playerType='AIR';
    ATSVersionNum="9";
    TestLevelNum="1";
    playerVersion="11,6,600,147";
    testSuite="0";
    ASVersionNum="3";
    client="ATS";
    plato="true";
    os="IOS";
#    //2 for Manual 
#    //1 for Automated
    TestTypeNum="2";
    isDebugger="0";
    osVersion="iPhone";

    urlStr="http://fpqa.macromedia.com/Sasquatch/AIRInformation/GenerateXML/buildProfileXML.cfm?"
    payload = {'playerType' :playerType ,'ATSVersionNum':ATSVersionNum,'TestLevelNum':TestLevelNum,'playerVersion':playerVersion,'testSuite':testSuite,'SVersionNum':ASVersionNum,'client':client,'plato':plato,'os':os,'TestTypeNum':TestTypeNum,'isDebugger':isDebugger,osVersion:'osVersion'}
    exp=urllib.urlencode(payload)
      
    request = urllib2.Request(urlStr+exp, headers={"Accept" : "application/xml"})
    print 'request object',request,request.data,request.get_full_url()
    response = urllib2.urlopen(request)
    
    tree = ElementTree.parse(response)
    print tree
    rootElem = tree.getroot()
    suite = client+ATSVersionNum
    testCaseInfoLst=[]
    recurse(rootElem, ' ')
#    for i in range(0,len(testPath)):
#        print testPath[i],testId[i]
##        testcase = TestCase('test_path'=testPath[i],'Suite'=suite,'test_caseiD'=testId[i]))
    for value in testCaseInfoLst:
        value.save();
    
    return HttpResponse("Welcome to D DashBoard page") 
    

    
     
    


def populateTestCaseInfoObject(path,node):
    tmpObject= TestCase();
    tmpObject.test_path=path;
    print path
    pathSplit = path.split('/')
    if pathSplit[2]=='AIR':
        print "in if"
        tmpObject.suite='AIR'
        tmpObject.test_area=pathSplit[3]
    else:
        tmpObject.suite=client+ATSVersionNum
        tmpObject.test_area=pathSplit[2]
    tmpObject.test_caseid=node.attrib.get('id')
    tmpObject.cr_dt=timezone.now().date();
    tmpObject.deleted_flag=False;
    tmpObject.cr_user='SYSTEM'
    tmpObject.swfName=node.tag
    tmpObject.lst_dt=timezone.now().date();
    tmpObject.lst_user='SYSTEM'
    return tmpObject


def recurse(node,path):
#    print val," ",node.tag,node.attrib
     if len(node._children)<=0:
        testCaseInfoLst.append(populateTestCaseInfoObject(path,node));
        
     else:
        for i in xrange(0,len(node._children)):
          str1=node.tag if len(path)==0 else path+'/'+node.tag
          recurse(node._children[i],str1)
       

#    if node.hasChildNodes():
#      for child in node:
#          recurse(child)
#    else:
#      print node    
    
    
    
