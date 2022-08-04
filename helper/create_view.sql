CREATE VIEW send_giftcard AS (
    WITH pets_owners AS (
        SELECT
            pets.petid,
            pets.petkind,
            pets.petname,
            owners.ownername || ' ' || owners.ownersurname AS full_name,
            owners
        FROM pets
        LEFT JOIN owners
            ON pets.ownerid=owners.ownerid
    )

    SELECT
        procedures_history.*,
        procedures_details.price,
        pets_owners.petkind,
        pets_owners.petname,
        pets_owners.full_name

    FROM procedures_history
    LEFT JOIN procedures_details
        ON procedures_history.proceduretype = procedures_details.proceduretype
                AND procedures_history.proceduresubcode = procedures_details.proceduresubcode
    LEFT JOIN pets_owners
                ON procedures_history.petid = pets_owners.petid
                                       )