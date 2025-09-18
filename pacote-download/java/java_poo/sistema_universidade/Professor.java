package sistema_universidade;

public class Professor extends Pessoa {
    // Atributos
    private double salario;
    private DepartamentoCursos departamento;

    // Construtor
    public Professor(String nome, int cpf, int idade, double salario) {
        super(nome, cpf, idade);
    }

    // Getters e setters
    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public DepartamentoCursos getDepartamento() {
        return departamento;
    }

    public void setDepartamento(DepartamentoCursos departamento) {
        this.departamento = departamento;
    }

    // Métodos
    public void ministrarAula(Disciplina d) {
        System.out.println("Ministrando aula.");
    }

    @Override
    public void mostrarInfo() {
       System.out.println("---------- INFORMAÇÕES ----------");
       System.out.println("Nome - " + getNome());
       System.out.println("CPF - " + getCpf());
       System.out.println("Idade - " + getIdade());
       System.out.println("Salário - " + getSalario());
       System.out.println("Departamento - " + getDepartamento());
    }
}
