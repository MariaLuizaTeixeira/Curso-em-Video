package sistema_universidade;

public class Aluno extends Pessoa {
    // Atributos
    private int matricula;
    private DepartamentoCursos curso;

    // Construtor
    public Aluno(String nome, int cpf, int idade, int matricula, DepartamentoCursos curso) {
        super(nome, cpf, idade);
    }

    // Getters e setters
     public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

     public DepartamentoCursos getCurso() {
        return curso;
    }

    public void setCurso(DepartamentoCursos curso) {
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
    
    public void realizarProva(Disciplina d) {
        System.out.println("Realizando prova.");
    }
}
