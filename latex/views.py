from django.shortcuts import render
from django.shortcuts import render_to_response
from markdown import markdown
import urllib.request
import re

# Create your views here.

def latex_equation(request):
	url=request.get_full_path()
	url=urllib.request.unquote(url)
	_r=re.findall(r"\?[\s\S]*",url) #匹配包括换行符
	if _r:
		equation_before=_r[0][1:] #去除?
	else:
		equation_before=""
	equation_after=markdown("$$%s$$"%equation_before,extensions=['tables'])
	contexts={'equation_after':equation_after,'equation_before':equation_before}
	return render_to_response('latex.html',contexts)