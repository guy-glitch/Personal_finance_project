#currency conversion file
import graphics

#function that does outer shell thing
def casing(which):
    ionc=False
    while True:
        try:
            money=float(graphics.inputs('USD value:',wrong=ionc))
            break
        except:
            ionc=True
    if which == 1:
        new=usd_eur(money)
    elif which==2:
        new=usd_jpy(money)
    elif which==3:
        new=usd_gbp(money)
    elif which==4:
        new=eur_usd(money)
    elif which==5:
        new=jpy_usd(money)
    else:
        new=gbp_usd(money)
    graphics.show(f'Original Value: {money}\nConverted Value: {new}')

#function that converts USD to EUR
def usd_eur(usd):
    return usd*0.85

#function that converts USD to JPY
def usd_jpy(usd):
    return usd*159.17

#function that converts USD to GBP
def usd_gbp(usd):
    return usd*0.74

#function that converts EUR to USD
def eur_usd(eur):
    return eur*1.17

#function that converts JPY to USD
def jpy_usd(jpy):
    return jpy*0.0063

#function that converts GBP to USD
def gbp_usd(gbp):
    return gbp*1.35