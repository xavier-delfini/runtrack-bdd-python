insert into laplateforme.etudiants(prenom, nom, age, email) values ('Martin', 'Dupuis',18,'martin.dupuis@laplateforme.io')
select * from laplateforme.etudiants where email in (
    select email from laplateforme.etudiants
    group by email having count(*) > 1
)