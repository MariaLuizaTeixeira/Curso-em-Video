package sistema_universidade;
public class Funcionario extends Pessoa{
    // Atributos
    private int id;
    private Cargo cargo;

    // Getters e setters
    public Cargo getCargo() {
        return cargo;
    }

    public void setCargo(Cargo cargo) {
        this.cargo = cargo;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    // Métodos
    @Override
     public void mostrarInfo() {
       System.out.println("---------- INFORMAÇÕES ----------");
       System.out.println("Nome - " + getNome());
       System.out.println("CPF - " + getCpf());
       System.out.println("Idade - " + getIdade());
       System.out.println("Cargo - " + getCargo());
    }

    public Funcionario(String nome, int cpf, int idade, Cargo cargo) {
        super(nome, cpf, idade);
        this.cargo = cargo;
    }

    public void executarTarefa() {
        System.out.println("Tarefa executada!");
    }
}
