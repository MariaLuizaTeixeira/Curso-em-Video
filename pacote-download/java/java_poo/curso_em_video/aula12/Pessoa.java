package aula12;

abstract class Pessoa {
    // Atributos
    protected String nome;
    protected int idade;
    protected String sexo;
    protected int experiencia;

    // Construtor
    public Pessoa(String nome, int idade, String sexo) {
        setNome(nome);
        setIdade(idade);
        setSexo(sexo);
        setExperiencia(0);
    }

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
    public int getExperiencia() {
        return experiencia;
    }
    public void setExperiencia(int experiencia) {
        this.experiencia = experiencia;
    }

    // Métodos
    protected void ganharExp() {
        
    }

    @Override
    public String toString() {
        return "Pessoa [nome=" + nome + ", idade=" + idade + ", sexo=" + sexo + ", experiencia=" + experiencia + "]";
    }

    
}
