def activity_select(start,finish,n):
    activity=[1]
    k=0
    for i in range(1, n):
        if(finish[k]<=start[i]):
            activity.append(i+1)
            k=i
    return activity

        
        
def rec_act_sel(start,finish,k,n,activity):
    m=k+1
    while( m<n and start[m]<finish[k] and k>=0):
        m=m+1

    if m<n:
        activity.append(m+1)
        rec_act_sel(start, finish, m,n,activity)
    
    return activity

        
        
        
