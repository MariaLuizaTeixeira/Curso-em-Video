package aula10;

public class Index {
    public static void main(String[] args) {
        Mamifero m = new Mamifero();
        Peixe p = new Peixe();
        // Reptil r = new Reptil();
        Ave a = new Ave();

        m.setPeso(85.3f);
        m.setIdade(2);
        m.setMembros(4);
        m.locomover();
        m.alimentar();
        m.emitirSom();

        p.setPeso(0.35f);
        p.setIdade(1);
        p.setMembros(0);
        p.locomover();
        p.alimentar();
        p.emitirSom();
        p.soltarBolha();

        a.setPeso(0.89f);
        a.setIdade(2);
        a.setMembros(2);
        a.locomover();
        a.alimentar();
        a.emitirSom();
        a.fazerNinho();
        /* 
        Canguru c = new Canguru();
        Cachorro k = new Cachorro();
        Cobra j = new Cobra();
        Arara e = new Arara();
        Tartaturuga t = new Tartaturuga();
        Goldfish g = new Goldfish();
        */


        m.setPeso(5.70f);
        m.setIdade(8);
        m.setMembros(4);
        m.locomover();
        m.alimentar();
        m.emitirSom();

        m.setPeso(5.70f);
        m.setIdade(8);
        m.setMembros(4);
        m.locomover();
        m.alimentar();
        m.emitirSom();
    }
}
