function  C = custom_dft(y, T, N, Nterm)

    medT = T/2;
    h = T/N;
    x_axis = -medT:h:medT;
    kMax = floor(2*Nterm*pi/T); 
       
    
    C = zeros(kMax, 1);

    for n = 0:kMax    
    
        argm = sum( y(x_axis).*exp(-1j*n.*x_axis))*10/N;
        C(n+1) = (2/pi)*argm; 

    end

end

