#Ask user for their name
s_Name=input('What is your name? ')

#Ask user for their current weight
n_earthWeight=input('What is your weight, in pounds? ')

#Convert Weight into float
n_earthWeight=float(n_earthWeight)

#Establish Surface Gravty Factor (SGF) for each of the planets
n_mercurySGF=0.38

n_venusSGF=0.91

n_moonSGF=0.165

n_marsSGF=0.38

n_jupiterSGF=2.34

n_saturnSGF=0.93

n_uranusSGF=0.92

n_neptuneSGF=1.12

n_plutoSGF=0.066

#Find weight for each planet via multiplying "Earth Weight" and their "SGF"
n_marsWeight=n_earthWeight*n_marsSGF

n_mercuryWeight=n_earthWeight*n_marsSGF

n_venusWeight=n_earthWeight*n_venusSGF

n_moonWeight=n_earthWeight*n_moonSGF

n_jupiterWeight=n_earthWeight*n_jupiterSGF

n_saturnWeight=n_earthWeight*n_saturnSGF

n_uranusWeight=n_earthWeight*n_uranusSGF

n_neptuneWeight=n_earthWeight*n_neptuneSGF

n_plutoWeight=n_earthWeight*n_plutoSGF

#Display weight for each respective planet, also display user's name
print(s_Name+" here are your weights on our Solar System's planets:")
print(f'Here is how much you would weigh on Mercury:   {n_mercuryWeight:>10.2f}')
print(f'Here is how much you would weigh on Venus:     {n_venusWeight:>10.2f}')
print(f'Here is how much you would weigh on Mars:      {n_marsWeight:>10.2f}')
print(f'Here is how much you would weigh on the Moon:  {n_moonWeight:>10.2f}')
print(f'Here is how much you would weigh on Jupiter:   {n_jupiterWeight:>10.2f}')
print(f'Here is how much you would weigh on Saturn:    {n_saturnWeight:>10.2f}')
print(f'Here is how much you would weigh on Uranus:    {n_uranusWeight:>10.2f}')
print(f'Here is how much you would weigh on Neptune:   {n_neptuneWeight:>10.2f}')
print(f'Here is how much you would weigh on Pluto:     {n_plutoWeight:>10.2f}')


