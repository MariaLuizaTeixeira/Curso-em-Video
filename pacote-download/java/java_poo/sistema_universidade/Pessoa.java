package sistema_universidade;

public abstract class Pessoa {
    // Atributos
    private String nome;
    private int cpf;
    private int idade;

    // Construtor
    public Pessoa(String nome, int cpf, int idade) {
        if (getIdade() < 0) {
            System.out.println("A idade não pode ser menor que 0.");
        }
        setNome(nome);
        setCpf(cpf);
        setIdade(idade);
    }

    // Getters e setters
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCpf() {
        return cpf;
    }

    public void setCpf(int cpf) {
        this.cpf = cpf;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    // Métodos
    public abstract void mostrarInfo();
}
