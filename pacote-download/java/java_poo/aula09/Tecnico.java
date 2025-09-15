package aula09;
public class Tecnico extends Aluno{
    // Atributos
    private int registroProfissional;

    // Getters e setters
    public int getRegistroProfissional() {
        return registroProfissional;
    }

    public void setRegistroProfissional(int registroProfissional) {
        this.registroProfissional = registroProfissional;
    }

    // Métodos
    public void praticar() {
        System.out.println("Praticando...");
    }
}
