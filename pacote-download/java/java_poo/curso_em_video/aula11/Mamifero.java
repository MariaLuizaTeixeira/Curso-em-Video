package aula11;

public class Mamifero extends Animal{
    // Atributos
    protected char corPelo;

    // Getters e setters
    public char getCorPelo() {
        return corPelo;
    }

    public void setCorPelo(char corPelo) {
        this.corPelo = corPelo;
    }
    
    // Métodos
    @Override
    public void locomover() {
        System.out.println("Correndo.");
    }

    @Override
    public void alimentar() {
        System.out.println("Mamando.");
    }

    @Override
    public void emitirSom() {
        System.out.println("Som de mamífero.");
    }
}
