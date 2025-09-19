package sistema_universidade;

public enum DepartamentoCursos {
    DEPENGENHARIA("Departamento de Engenharia") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 0;
    }
    },
    DEPDIREITO("Departamento de Direito") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 0;
    }
    },
    DEPMEDICINA("Departamento de Medicina") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 0;
    }
    },
    DEPCOMPUTACAO("Departamento de Ciência da Computação") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 0;
    }
    },
    ENGENHARIA("Engenharia") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 3600;
    }
    },
    DIREITO("Direito") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 3000;
    }
    },
    MEDICINA("Medicina") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 4000;
    }
    },
    COMPUTACAO("Ciência da Computação") {
        @Override
        public int getCarga_horaria_minima(int carga_horaria_minima) {
        return 3200;
    }
    };

    private final String nome;

    DepartamentoCursos(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public abstract int getCarga_horaria_minima(int carga_horaria_minima);
}
