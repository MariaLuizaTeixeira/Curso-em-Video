package sistema_universidade;

public class Aluno extends Pessoa {

    // Atributos
    private int matricula;
    private Curso curso;

    // Construtor
    public Aluno(String nome, int cpf, int idade, int matricula, Curso curso) {
        super(nome, cpf, idade);
    }

    // Getters e setters
     public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

     public Curso getCurso() {
        return curso;
    }

    public void setCurso(Curso curso) {
        this.curso = curso;
    }

    // Métodos
    @Override
    public void mostrarInfo() {
       System.out.println("---------- INFORMAÇÕES ----------");
       System.out.println("Nome - " + getNome());
       System.out.println("CPF - " + getCpf());
       System.out.println("Idade - " + getIdade());
    }
    
    public void realizarProva() {
        System.out.println("Realizando prova.");
    }
}
