WITH december_procedures AS (
    SELECT procedureid, date
    FROM send_giftcard
    WHERE EXTRACT(MONTH FROM date) = 12
)

SELECT send_giftcard.petname,
       send_giftcard.petkind,
       send_giftcard.owner_fullname,
       send_giftcard.zipcode
FROM send_giftcard AS send_giftcard
INNER JOIN december_procedures
    ON send_giftcard.procedureid = december_procedures.procedureid