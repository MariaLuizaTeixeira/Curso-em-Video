package aula12;

public class Gafanhoto extends Pessoa{
    // Atributos
    private String login;
    private int totAssistido;

    // Construtor
    public Gafanhoto(String nome, int idade, String sexo, String login) {
        super(nome, idade, sexo);
        setLogin(login);
        setTotAssistido(0);

    }

    // Getters e setters
    public String getLogin() {
        return login;
    }
    public void setLogin(String login) {
        this.login = login;
    }
    public int getTotAssistido() {
        return totAssistido;
    }
    public void setTotAssistido(int totAssistido) {
        this.totAssistido = totAssistido;
    }

    // Metodos
    public void viuMaisUm() {

    }

    @Override
    public String toString() {
        return "Gafanhoto [" + super.toString() + "login=" + login + ", totAssistido=" + totAssistido + "]";
    }

    
}
