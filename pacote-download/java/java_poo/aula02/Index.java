package aula02;
public class Index {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.cor = "Azul";
        c1.modelo = "BIC Cristal";
       // c1.ponta = 0.5f;
       c1.carga = 80;
       // c1.tampada = false;
        c1.destampar();
        c1.status();
        c1.rabiscar();
        

        /* Caneta c2 = new Caneta();
        c2.modelo = "Hosnet";
        c2.cor = "Preta";
        c2.destampar();
        c2.rabiscar();
        */
    }
}
