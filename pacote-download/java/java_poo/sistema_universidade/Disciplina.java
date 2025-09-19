package sistema_universidade;
import java.util.ArrayList;
import java.util.Scanner;

public class Disciplina {
    // Atributos
    private String nome;
    private int carga_horaria;
    private Professor professor_responsavel;
    private String alunos[];
    private Aluno a;

    // Getters e setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getCarga_horaria() {
        return carga_horaria;
    }
    public void setCarga_horaria(int carga_horaria) {
        this.carga_horaria = carga_horaria;
    }
    public Professor getProfessor() {
        return professor_responsavel;
    }
    public void setProfessor(Professor professor) {
        this.professor_responsavel = professor;
    }
    public String[] getAlunos() {
        return alunos;
    }
    public void setAlunos(String[] alunos) {
        this.alunos = alunos;
    }

    public Professor getProfessor_responsavel() {
        return professor_responsavel;
    }
    public void setProfessor_responsavel(Professor professor_responsavel) {
        this.professor_responsavel = professor_responsavel;
    }
    public Aluno getA() {
        return a;
    }
    public void setA(Aluno a) {
        this.a = a;
    }

    // Métodos
    public void adicionarAluno(Aluno a) {
        Scanner scanner = new Scanner(System.in);
        ArrayList alunos = new ArrayList();
        Disciplina d1 = new Disciplina();
        System.out.println("Insira o nome da disciplina");
        setNome(scanner.nextLine());
        System.out.println("Insira o nome do aluno");
        a.setNome(scanner.nextLine());
        alunos.add(a);
        scanner.close();
    }    
}
