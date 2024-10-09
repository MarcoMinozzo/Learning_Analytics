Para identificar as inscrições realizadas no último mês em um curso no Moodle, você pode seguir estas etapas usando **consultas SQL** ou plugins como o **Configurable Reports** ou **Ad-hoc database queries**. Aqui está um caminho usando o plugin Configurable Reports:

### Passos:

1. **Instale o plugin Configurable Reports** (se ainda não estiver instalado):
   - Acesse o painel de administração do Moodle.
   - Vá para **Site administration > Plugins > Install plugins** e instale o plugin [Configurable Reports](https://moodle.org/plugins/block_configurable_reports).

2. **Crie um novo relatório personalizado**:
   - Acesse **Site administration > Reports > Configurable Reports**.
   - Clique em **Create a new report**.
   - Selecione **SQL Report** como o tipo de relatório.

3. **Consulta SQL para inscrições no último mês**:

Aqui está uma consulta SQL para identificar as inscrições no último mês em um curso específico:

```sql
SELECT u.id AS UserID, 
       u.firstname AS FirstName, 
       u.lastname AS LastName, 
       u.email AS Email, 
       FROM_UNIXTIME(ue.timecreated, '%Y-%m-%d') AS EnrollmentDate
FROM mdl_user u
JOIN mdl_user_enrolments ue ON ue.userid = u.id
JOIN mdl_enrol e ON e.id = ue.enrolid
JOIN mdl_course c ON c.id = e.courseid
WHERE c.id = [ID_DO_CURSO]
AND ue.timecreated >= UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
ORDER BY ue.timecreated DESC;
```

#### Explicação:
- **`mdl_user`**: Tabela que armazena os dados dos usuários.
- **`mdl_user_enrolments`**: Tabela que registra as inscrições dos usuários.
- **`mdl_enrol`**: Tabela que liga os usuários ao curso.
- **`mdl_course`**: Tabela dos cursos do Moodle.
- **`c.id = [ID_DO_CURSO]`**: Substitua `[ID_DO_CURSO]` pelo ID do curso em que você deseja verificar as inscrições.
- **`ue.timecreated >= UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))`**: Seleciona apenas as inscrições feitas nos últimos 30 dias.

4. **Visualizar o relatório**:
   - Após executar a consulta, o relatório vai mostrar todos os usuários inscritos no último mês, com a data de inscrição.

### Alternativas:
- Se preferir algo sem SQL, pode usar os relatórios padrões do Moodle:
  - **Relatórios de usuários inscritos**: Acesse o curso em questão, vá até **Participantes** e filtre por **data de inscrição**.

Essas abordagens permitem identificar as inscrições recentes de maneira prática e automatizada. Se precisar de mais detalhes ou ajustes, me avise!
