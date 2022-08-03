CREATE TABLE IF NOT EXISTS owners(

    OwnerID CHAR(4) PRIMARY KEY NOT NULL,
    OwnerName VARCHAR NOT NULL,
    OwnerSurname VARCHAR NOT NULL,
    StreetAddress VARCHAR NOT NULL,
    City VARCHAR NOT NULL,
    State CHAR(2) NOT NULL,
    StateFull VARCHAR NOT NULL,
    ZipCode CHAR(5) NOT NULL
);

CREATE TABLE IF NOT EXISTS pets(

    PetID CHAR(7) PRIMARY KEY NOT NULL,
    PetName VARCHAR NOT NULL,
    PetKind VARCHAR NOT NULL,
    PetGender VARCHAR NOT NULL,
    PetAge SMALLINT NOT NULL,
    OwnerID CHAR(4) NOT NULL,

    CONSTRAINT fk_owners
        FOREIGN KEY (OwnerID)
        REFERENCES owners(OwnerID)
);

CREATE TABLE IF NOT EXISTS procedures_details(

    ProcedureType VARCHAR NOT NULL,
    ProcedureSubCode CHAR(2) NOT NULL,
    Description TEXT,
    Price NUMERIC NOT NULL,

    PRIMARY KEY (ProcedureType, ProcedureSubCode)
);

CREATE TABLE IF NOT EXISTS procedures_history(

    ProcedureID SERIAL PRIMARY KEY,
    PetID CHAR(7) NOT NULL,
    Date DATE NOT NULL,
    ProcedureType VARCHAR NOT NULL,
    ProcedureSubCode CHAR(2) NOT NULL,

    CONSTRAINT fk_procedures
        FOREIGN KEY (ProcedureType, ProcedureSubCode)
            REFERENCES procedures_details(ProcedureType, ProcedureSubCode),

    CONSTRAINT fk_pets
        FOREIGN KEY (PetID)
            REFERENCES pets(PetID)
)
