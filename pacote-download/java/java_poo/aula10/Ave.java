package aula10;
public class Ave extends Animal{
    // Atributos
    private char corPena;

    // Getters e setters
    public char getCorPena() {
        return corPena;
    }

    public void setCorPena(char corPena) {
        this.corPena = corPena;
    }
    
    // Métodos
    @Override
    public void locomover() {
        System.out.println("Voando.");
    }

    @Override
    public void alimentar() {
        System.out.println("Comendo frutas.");
    }

    @Override
    public void emitirSom() {
        System.out.println("Som de ave.");
    }

    public void fazerNinho() {
        System.out.println("Construindo um ninho.");
    }
}

