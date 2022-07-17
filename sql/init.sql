BEGIN;


CREATE TABLE IF NOT EXISTS public.anime
(
    anime_id uuid NOT NULL,
    synopsis text,
    url character varying(200) NOT NULL,
    title character varying(100) NOT NULL,
    jtitle character varying(100) NOT NULL,
    CONSTRAINT anime_pk PRIMARY KEY (anime_id),
    CONSTRAINT unique_url UNIQUE (url),
    CONSTRAINT unique_title UNIQUE (title),
    CONSTRAINT unique_jtitle UNIQUE (jtitle)
);

CREATE TABLE IF NOT EXISTS public.producers
(
    producers_id serial,
    name character varying(50) NOT NULL,
    CONSTRAINT producer_pk PRIMARY KEY (producers_id),
    CONSTRAINT producers_unique_name UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.licensors
(
    licensors_id serial,
    name character varying(50) NOT NULL,
    CONSTRAINT licensors_pk PRIMARY KEY (licensors_id),
    CONSTRAINT licensors_unique_name UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.studios
(
    studios_id serial,
    name character varying,
    CONSTRAINT studios_pk PRIMARY KEY (studios_id),
    CONSTRAINT studios_unique_name UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.anime_producers
(
    anime_producers_id serial,
    anime_info_id integer NOT NULL,
    producers_id integer NOT NULL,
    CONSTRAINT anime_producers_pk PRIMARY KEY (anime_producers_id)
);

CREATE TABLE IF NOT EXISTS public.anime_licensors
(
    anime_licensors_id serial,
    anime_info_id integer NOT NULL,
    licensors_id integer NOT NULL,
    CONSTRAINT anime_licensors_pk PRIMARY KEY (anime_licensors_id)
);

CREATE TABLE IF NOT EXISTS public.anime_studios
(
    anime_studios_id serial,
    anime_info_id integer NOT NULL,
    studios_id integer NOT NULL,
    CONSTRAINT anime_studios_pk PRIMARY KEY (anime_studios_id)
);

CREATE TABLE IF NOT EXISTS public.anime_statistics
(
    anime_stats_id serial,
    anime_id uuid NOT NULL,
    score numeric(3, 2),
    ranked integer,
    popularity integer,
    members integer,
    favorites integer,
    CONSTRAINT anime_stats_pk PRIMARY KEY (anime_stats_id)
);

CREATE TABLE IF NOT EXISTS public.anime_info
(
    anime_info_id serial,
    anime_type character varying(10),
    n_episodes integer,
    status character varying(20),
    aired character varying(50),
    premiered character varying(50),
    broadcast character varying(50),
    "source " character varying(50),
    demographic character varying(50),
    duration interval,
    rating character varying(100),
    anime_id uuid,
    CONSTRAINT anime_info_pk PRIMARY KEY (anime_info_id)
);

ALTER TABLE IF EXISTS public.anime_producers
    ADD CONSTRAINT anime_info_fk FOREIGN KEY (anime_info_id)
    REFERENCES public.anime_info (anime_info_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_producers
    ADD CONSTRAINT producers_fk FOREIGN KEY (producers_id)
    REFERENCES public.producers (producers_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_licensors
    ADD CONSTRAINT anime_info_fk FOREIGN KEY (anime_info_id)
    REFERENCES public.anime_info (anime_info_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_licensors
    ADD CONSTRAINT anime_licensors_fk FOREIGN KEY (licensors_id)
    REFERENCES public.licensors (licensors_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_studios
    ADD CONSTRAINT anime_info_fk FOREIGN KEY (anime_info_id)
    REFERENCES public.anime_info (anime_info_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_studios
    ADD CONSTRAINT studios_fk FOREIGN KEY (studios_id)
    REFERENCES public.studios (studios_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_statistics
    ADD CONSTRAINT anime_fk FOREIGN KEY (anime_id)
    REFERENCES public.anime (anime_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.anime_info
    ADD CONSTRAINT anime_fk FOREIGN KEY (anime_id)
    REFERENCES public.anime (anime_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
