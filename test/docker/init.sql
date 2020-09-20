--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6
-- Dumped by pg_dump version 10.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: aquifers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aquifers (
    id integer NOT NULL,
    materials text,
    productivity text,
    vulnerability text,
    demand text,
    location_description text,
    url text,
    type_of_water_use text,
    geom public.geometry
);


ALTER TABLE public.aquifers OWNER TO postgres;

--
-- Name: aquifers_detail; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aquifers_detail (
    id integer NOT NULL,
    materials text,
    productivity text,
    vulnerability text,
    demand text,
    location_description text,
    url text,
    type_of_water_use text,
    geom public.geometry
);


ALTER TABLE public.aquifers_detail OWNER TO postgres;

--
-- Name: aquifers_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aquifers_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aquifers_detail_id_seq OWNER TO postgres;

--
-- Name: aquifers_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aquifers_detail_id_seq OWNED BY public.aquifers_detail.id;


--
-- Name: aquifers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aquifers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aquifers_id_seq OWNER TO postgres;

--
-- Name: aquifers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aquifers_id_seq OWNED BY public.aquifers.id;


--
-- Name: culverts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.culverts (
    id integer NOT NULL,
    name character varying,
    geom public.geometry(Point,4326)
);


ALTER TABLE public.culverts OWNER TO postgres;

--
-- Name: culverts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.culverts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.culverts_id_seq OWNER TO postgres;

--
-- Name: culverts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.culverts_id_seq OWNED BY public.culverts.id;


-- noinspection SqlNoDataSourceInspection

CREATE TABLE public.field_observations (
    uuid uuid,
    coordinates public.geometry,
    calculated_flow_rate text,
    json_record json
);

ALTER TABLE public.field_observations OWNER TO postgres;
ALTER TABLE ONLY public.field_observations ADD CONSTRAINT field_observations_uuid_key UNIQUE (uuid);

CREATE VIEW public.v_all_points AS
SELECT uuid,
       coordinates AS where_am_i,
       (json_record ->> 'created_at')::timestamp without time zone AS created_at,
       (NULLIF(json_record ->> 'temperature_water', ''::text))::double precision AS temperature,
       (NULLIF(json_record ->> 'conductivity', ''::text))::double precision AS conductivity,
       (NULLIF(json_record ->> 'ph_oakton', ''::text))::double precision AS ph,
       (NULLIF(calculated_flow_rate, ''::text))::double precision AS flow_rate,
       (NULLIF(json_record ->> 'alkalinity', ''::text))::double precision AS alkalinity,
       (NULLIF(json_record ->> 'hardness', ''::text))::double precision AS hardness,
       (NULLIF(json_record ->> 'dissolved_oxygen', ''::text))::double precision AS dissolved_oxygen
FROM public.field_observations;


--
-- Name: faults; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faults (
    id integer NOT NULL,
    name character varying,
    geom public.geometry(LineStringZ,4326)
);


ALTER TABLE public.faults OWNER TO postgres;

--
-- Name: faults_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faults_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faults_id_seq OWNER TO postgres;

--
-- Name: faults_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faults_id_seq OWNED BY public.faults.id;


--
-- Name: geology; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.geology (
    id integer NOT NULL,
    name text,
    description text,
    geom public.geometry
);


ALTER TABLE public.geology OWNER TO postgres;

--
-- Name: geology_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.geology_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.geology_id_seq OWNER TO postgres;

--
-- Name: geology_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.geology_id_seq OWNED BY public.geology.id;


--
-- Name: greenwood; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.greenwood (
    id integer NOT NULL,
    geom public.geometry
);


ALTER TABLE public.greenwood OWNER TO postgres;

--
-- Name: greenwood_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.greenwood_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.greenwood_id_seq OWNER TO postgres;

--
-- Name: greenwood_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.greenwood_id_seq OWNED BY public.greenwood.id;


--
-- Name: parcel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parcel (
    id integer NOT NULL,
    geom public.geometry
);


ALTER TABLE public.parcel OWNER TO postgres;

--
-- Name: parcel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parcel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parcel_id_seq OWNER TO postgres;

--
-- Name: parcel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parcel_id_seq OWNED BY public.parcel.id;


--
-- Name: parcels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parcels (
    id integer NOT NULL,
    geom public.geometry
);


ALTER TABLE public.parcels OWNER TO postgres;

--
-- Name: parcels_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parcels_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parcels_id_seq OWNER TO postgres;

--
-- Name: parcels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parcels_id_seq OWNED BY public.parcels.id;


--
-- Name: spring; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spring (
    id integer NOT NULL,
    stream_name text,
    purpose text,
    quantity double precision,
    units text,
    geom public.geometry
);


ALTER TABLE public.spring OWNER TO postgres;

--
-- Name: spring_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spring_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.spring_id_seq OWNER TO postgres;

--
-- Name: spring_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spring_id_seq OWNED BY public.spring.id;


--
-- Name: springs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.springs (
    id integer NOT NULL,
    stream_name text,
    purpose text,
    quantity double precision,
    units text,
    geom public.geometry
);


ALTER TABLE public.springs OWNER TO postgres;

--
-- Name: springs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.springs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.springs_id_seq OWNER TO postgres;

--
-- Name: springs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.springs_id_seq OWNED BY public.springs.id;


--
-- Name: stream_network; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stream_network (
    id integer NOT NULL,
    name text,
    geom public.geometry
);


ALTER TABLE public.stream_network OWNER TO postgres;

--
-- Name: stream_network_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stream_network_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stream_network_id_seq OWNER TO postgres;

--
-- Name: stream_network_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stream_network_id_seq OWNED BY public.stream_network.id;

--
-- Name: watersheds_crd; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.watersheds_crd (
    id integer NOT NULL,
    name text,
    description text,
    geom public.geometry
);


ALTER TABLE public.watersheds_crd OWNER TO postgres;

--
-- Name: watersheds_crd_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.watersheds_crd_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.watersheds_crd_id_seq OWNER TO postgres;

--
-- Name: watersheds_crd_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.watersheds_crd_id_seq OWNED BY public.watersheds_crd.id;


--
-- Name: wells; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.wells (
    id integer NOT NULL,
    water_depth double precision,
    bedrock_depth double precision,
    elevation double precision,
    general_remarks text,
    yield_value double precision,
    url text,
    geom public.geometry
);


ALTER TABLE public.wells OWNER TO postgres;

--
-- Name: wells_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.wells_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wells_id_seq OWNER TO postgres;

--
-- Name: wells_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.wells_id_seq OWNED BY public.wells.id;


--
-- Name: aquifers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aquifers ALTER COLUMN id SET DEFAULT nextval('public.aquifers_id_seq'::regclass);


--
-- Name: aquifers_detail id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aquifers_detail ALTER COLUMN id SET DEFAULT nextval('public.aquifers_detail_id_seq'::regclass);


--
-- Name: culverts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.culverts ALTER COLUMN id SET DEFAULT nextval('public.culverts_id_seq'::regclass);


--
-- Name: faults id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faults ALTER COLUMN id SET DEFAULT nextval('public.faults_id_seq'::regclass);


--
-- Name: geology id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.geology ALTER COLUMN id SET DEFAULT nextval('public.geology_id_seq'::regclass);


--
-- Name: greenwood id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.greenwood ALTER COLUMN id SET DEFAULT nextval('public.greenwood_id_seq'::regclass);


--
-- Name: parcel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcel ALTER COLUMN id SET DEFAULT nextval('public.parcel_id_seq'::regclass);


--
-- Name: parcels id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcels ALTER COLUMN id SET DEFAULT nextval('public.parcels_id_seq'::regclass);


--
-- Name: spring id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spring ALTER COLUMN id SET DEFAULT nextval('public.spring_id_seq'::regclass);


--
-- Name: springs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.springs ALTER COLUMN id SET DEFAULT nextval('public.springs_id_seq'::regclass);


--
-- Name: stream_network id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stream_network ALTER COLUMN id SET DEFAULT nextval('public.stream_network_id_seq'::regclass);


--
-- Name: watersheds_crd id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watersheds_crd ALTER COLUMN id SET DEFAULT nextval('public.watersheds_crd_id_seq'::regclass);


--
-- Name: wells id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wells ALTER COLUMN id SET DEFAULT nextval('public.wells_id_seq'::regclass);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

