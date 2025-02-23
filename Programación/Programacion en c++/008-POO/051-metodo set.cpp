# include <iostream>

class Persona{
    private:
        int edad = 0;
        std::string nombre = "";
    
     public:
        int getEdad (){
       return edad;     
    }
        void setEdad(int nuevaedad){
            edad = nuevaedad;
        }
};

int main(){
    Persona* persona1 = new Persona();
    std::cout << persona1->edad << std::endl;
    persona1.setEdad(5);
    std::cout << persona1->edad << std::endl;
    return 0;
}