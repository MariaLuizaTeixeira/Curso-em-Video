import java.util.Date;
import java.util.Locale;
import java.awt.Dimension;
import java.awt.Toolkit;

public class PrimeiroPrograma {
    public static void main(String[] args) {
        System.out.println("Olá mundo!");
        Date relogio = new Date();
        System.out.println("A hora do sistema é: ");
        System.out.println(relogio.toString());
        Locale Idioma = Locale.getDefault();
        System.out.println("O idioma da aplicação é: ");
        System.out.println(Idioma);
        Dimension size = Toolkit.getDefaultToolkit().getScreenSize();
        int largura = (int)size.getWidth();
        int altura = (int)size.getHeight();
        System.out.println("Sua resolução é de:"
        + " " + largura
        + " X " + altura);
    }
}

