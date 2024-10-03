a=[{'Name':'Hello','wc':5},
   {'Name':'Hi','wc':2},
   {'Name':'Bye','wc':3},
   {'Name':'Python','wc':6},
   {'Name':'C','wc':1}
   
   ]
print(a)
ans=filter(lambda var:var['wc']>2,a)
ans=list(ans)
print(ans)