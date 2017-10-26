# CHAOS-6 Modelo de Campo Geomagnético 

*Autores: Christopher C. Finlay¹, Nils Olsen¹, Stavros Kotsiaros¹, Nicolas Gillet², and Lars Toeffner-Clausen¹

* website [chaos-6](http://www.spacecenter.dk/files/magnetic-models/CHAOS-6/)

1 DTU Space, National Space Institute, Technical University of Denmark, Elektrovej 327, 2800 Kgs. Lyngby, Denmark.
2 ISTerre, Universite Grenoble 1, and CNRS, Grenoble, France.



***Estas pastas contém os códigos e os dados necessários para gerar o modelo do campo magnético terrestre interno, externo e total.*** 

- [ ] `covert.m` é uma código em matlab que utiliza funções internas para converter dados no formato (AAAA MM DD Hora Min Seg) para juliandate que é o formato ulitilazdo para pelo programa `synth_CHAOS_preds` para geração dos modelos. (Mais informações sobre as funções, veja o arquivo `about_convert`)










--



***Summary
We use more than two years of magnetic data from the Swarm mission, and monthly means from 160 ground observatories as available in March 2016, to update the CHAOS time-dependent geomagnetic field model. The new model, CHAOS-6, provides information on time variations of the core-generated part of the Earth's magnetic field between 1999.0 and 2016.5. 

***We present details of the secular variation (SV) and secular acceleration (SA) from CHAOS-6 at Earth's surface and downward continued to the core surface. At Earth's surface, we find evidence for positive acceleration of the field intensity in 2015 over a broad area around longitude 90 deg E that is also seen at ground observatories such as Novosibirsk. At the core surface, we are able to map the SV up to degree 16. The radial field SA at the core surface in 2015 is found to be largest at low latitudes under the India-South East Asia region, under the region of northern South America, and at high northern latitudes under Alaska and Siberia. Surprisingly, there is also evidence for significant SA in the central Pacific region, for example near Hawaii where radial field SA is observed on either side of a jerk in 2014. On the other hand, little SV or SA has occurred over the past 17 years in the Southern polar region. Inverting for a quasi-geostrophic core flow that accounts for this SV, we obtain a prominent planetary-scale, anti-cyclonic, gyre centered on the Atlantic hemisphere. We also find oscillations of non-axisymmetric, azimuthal, jets at low latitudes, for example close to 40deg W, that may be responsible for localized SA oscillations. 

In addition to scalar data from Oersted, CHAMP, SAC-C and Swarm, and vector data from Oersted, CHAMP and Swarm, CHAOS-6 benefits from the inclusion of along-track differences of scalar and vector field data from both CHAMP and the three Swarm satellites, as well as east-west differences between the lower pair of Swarm satellites, Alpha and Charlie. Moreover, ground observatory SV estimates are fit to a Huber-weighted rms level of 3.1 nT/yr for the eastward components and 3.8 and 3.7 nT/yr for the vertical and southward components. We also present an update of the CHAOS high degree lithospheric field, making use of along-track differences of CHAMP scalar and vector field data to produce a new static field model that agrees well with the MF7 field model (Maus, 2010) out to degree 110. 

Reference
Finlay, C.C., Olsen, N., Kotsiaros, S., Gillet, N. and Toeffner-Clausen, L., (2016) Recent geomagnetic secular variation from Swarm and ground observatories as estimated in the CHAOS-6 geomagnetic field model. Earth, Planets, Space, 68, 112, doi: 10.1186/s40623-016-0486-1
