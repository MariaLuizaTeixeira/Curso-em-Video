package aula12;

public class Video implements AcoesVideo {
    // Atributos
    private String titulo;
    private int avaliacao;
    private int views;
    private int curtidas;
    private boolean reproduzindo;

    // Construtor
    public Video(String titulo) {
        setTitulo(titulo);
        setAvaliacao(1);
        setViews(0);
        setCurtidas(0);
        setReproduzindo(false);
    }

    // Getters e setters
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(int avaliacao) {
        int nova;
        nova = (getAvaliacao() + avaliacao) / getViews();
    }

    public int getViews() {
        return views;
    }

    public void setViews(int views) {
        this.views = views;
    }

    public int getCurtidas() {
        return curtidas;
    }

    public void setCurtidas(int curtidas) {
        this.curtidas = curtidas;
    }

    public boolean isReproduzindo() {
        return reproduzindo;
    }

    public void setReproduzindo(boolean reproduzindo) {
        this.reproduzindo = reproduzindo;
    }

    // Métodos
    @Override
    public void play() {
        setReproduzindo(true);
    }

    @Override
    public void pause() {
        setReproduzindo(false);
    }

    @Override
    public void like() {
        setCurtidas(getCurtidas() + 1);
    }

    // toString
    @Override
    public String toString() {
        return "Video [titulo=" + titulo + ", avaliacao=" + avaliacao + ", views=" + views + ", curtidas=" + curtidas
                + ", reproduzindo=" + reproduzindo + "]";
    }

    
}
