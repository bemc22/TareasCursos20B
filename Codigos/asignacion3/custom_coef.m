function  C = custom_coef(y, T, N, Nterm)

    medT = T/2;
    h = T/N;
    x_axis = -medT:h:medT;       
    
    C = zeros(Nterm, 1);
    
    for n = 0:Nterm    
    
        argm = sum( y(x_axis).*exp(-1j*(n*2*pi/T).*x_axis));
        C(n+1) = argm*(2/T)*(20/N); 
    
    end
end

