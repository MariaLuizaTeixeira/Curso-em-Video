package aula09;
abstract class Pessoa {
    // Atributos
    private String nome;
    private int idade;
    private String sexo;

    // Getters e setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }
    public String getSexo() {
        return sexo;
    }
    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    // Metodos
    public void fazerAniversario() {
        setIdade(getIdade() + 1);
    }

    @Override
    public String toString() {
        return "Dados:\n Nome - " + nome + "\nIdade - " + idade + "\nSexo - " + sexo;
    }
}
