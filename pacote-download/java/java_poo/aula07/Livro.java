package aula07;

public class Livro implements Publicacao {

    // Atributos
    private String titulo;
    private String autor;
    private int totPaginas;
    private int pagAtual;
    private boolean aberto;
    private Pessoa leitor;

    // Construtor
    public Livro(String titulo, String autor, int totPaginas, Pessoa leitor) {
        this.titulo = titulo;
        this.autor = autor;
        this.totPaginas = totPaginas;
        this.leitor = leitor;
    }

    // Getters e setters
    public String getTitulo() {
        return titulo;
    }

    public Livro() {
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getTotPaginas() {
        return totPaginas;
    }

    public void setTotPaginas(int totPaginas) {
        this.totPaginas = totPaginas;
    }

    public int getPagAtual() {
        return pagAtual;
    }

    public void setPagAtual(int pagAtual) {
        this.pagAtual = pagAtual;
    }

    public boolean isAberto() {
        return aberto;
    }

    public void setAberto(boolean aberto) {
        this.aberto = aberto;
    }

    public Pessoa getLeitor() {
        return leitor;
    }

    // Métodos
    public String detalhes() {
        return "LIVRO:\nTítulo - " + titulo + "\nAutor - " + autor + "\nTotal de páginas - " + totPaginas + "\nPágina atual - " + pagAtual
                + "\nEstá aberto? " + aberto + "\nLeitor - " + leitor.getNome();
    }

    @Override
    public void abrir() {
        setAberto(true);
    }

    @Override
    public void fechar() {
        setAberto(false);
    }

    @Override
    public void avancarPag() {
        setPagAtual(getPagAtual() + 1);
    }

    @Override
    public void voltarPag() {
        setPagAtual(getPagAtual() - 1);
    }

    @Override
    public void folhear(int p) {
        if (p > getTotPaginas()) {
            System.out.println("Não é possível ir para a página " + p + ", o livro só tem " + getTotPaginas() + " páginas.");
        }
        setPagAtual(p);
    }
}
