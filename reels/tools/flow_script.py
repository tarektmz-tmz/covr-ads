"""Turn an approved script into 'flow text' for HeyGen: no punctuation, no symbols, numbers written as words,
one continuous line. Punctuation (. , ; : ! ? - ' etc.) and commas inside numbers make the voice pause.
usage: python3 flow_script.py script.txt   (prints the flow text)
"""
import re,sys
ONES="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"
def words(n):
    if n<20:return ONES[n]
    if n<100:return TENS[n//10]+("" if n%10==0 else " "+ONES[n%10])
    if n<1000:return ONES[n//100]+" hundred"+("" if n%100==0 else " "+words(n%100))
    if n<1000000:return words(n//1000)+" thousand"+("" if n%1000==0 else " "+words(n%1000))
    return words(n//1000000)+" million"+("" if n%1000000==0 else " "+words(n%1000000))
def year(n):
    h,t=divmod(n,100)
    if n==2000:return "two thousand"
    if 2000<n<2010:return "two thousand "+ONES[t]
    return words(h)+" "+("oh "+ONES[t] if 0<t<10 else (words(t) if t else "hundred"))
CONTR={"it's":"it is","that's":"that is","i'm":"i am","don't":"do not","can't":"cannot","won't":"will not","you'll":"you will","we'll":"we will","there's":"there is","what's":"what is","let's":"let us","doesn't":"does not","isn't":"is not","didn't":"did not","you're":"you are","we're":"we are","they're":"they are","i'll":"i will","i've":"i have","you've":"you have"}
def flow(t):
    t=t.replace("’","'")
    t=re.sub(r"\$\s?(\d[\d,]*)(\.\d+)?",lambda m:" "+words(int(m.group(1).replace(",","")))+" dollars ",t)
    t=re.sub(r"(\d[\d,]*)\s?%",lambda m:" "+words(int(m.group(1).replace(",","")))+" percent ",t)
    t=re.sub(r"(\d+)\s?mm\b",lambda m:" "+words(int(m.group(1)))+" millimeter ",t)
    def num(m):
        v=int(m.group(0).replace(",",""))
        return " "+(year(v) if 1900<=v<=2099 else words(v))+" "
    t=re.sub(r"\d[\d,]*",num,t)
    for k,v in CONTR.items():t=re.sub(r"\b"+re.escape(k)+r"\b",v,t,flags=re.I)
    t=re.sub(r"[-–—/]"," ",t)
    t=re.sub(r"[^A-Za-z0-9 \n]"," ",t)
    t=re.sub(r"\s+"," ",t).strip()
    return t
if __name__=="__main__":
    print(flow(open(sys.argv[1]).read()))
