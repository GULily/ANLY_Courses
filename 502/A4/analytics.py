def google_analytics(url):
    from subprocess import Popen,PIPE
    code = Popen(['curl','-s','-L',url],stdout=PIPE).communicate()[0].decode('utf-8','ignore')
    if "analytics.js" in code:
        return True
    if "ga.js" in code:
        return True
    else:
        return False
