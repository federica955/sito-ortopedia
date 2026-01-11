import streamlit as st

# Configurazione della pagina (Titolo che appare nella scheda del browser)
st.set_page_config(page_title="Dr. Domenico Franco - Ortopedico", page_icon="⚕️", layout="centered")

# --- HEADER PROFESSIONALE ---
st.title("Dr. Domenico Franco")
st.subheader("Specialista in Ortopedia e Traumatologia")

# --- SEZIONE BIOGRAFIA ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Profilo Professionale
    Il **Dr. Domenico Franco** è un Medico Chirurgo specializzato in **Ortopedia e Traumatologia**. 
    Si dedica alla diagnosi e al trattamento delle patologie dell'apparato locomotore, 
    con particolare attenzione alle tecniche chirurgiche d'avanguardia e alla cura del paziente 
    nel percorso riabilitativo.
    """)
    st.info("🎓 Specializzazione conseguita presso [Nome Università/Ospedale]")

with col2:
    # Qui potrai caricare una foto reale in futuro
    st.image("https://www.w3schools.com/howto/img_avatar.png", caption="Dr. Domenico Franco")

st.divider()

# --- AMBITI DI INTERVENTO ---
st.header("🎯 Ambiti di Intervento")
c1, c2, c3 = st.columns(3)

with c1:
    st.write("**Tecniche rigenerative della cartilagine**")
    st.caption("Sports medicine ")
with c2:
    st.write("**Anca e Ginocchio**")
    st.caption("Lesioni legamentose e meniscali")
with c3:
    st.write("**Chirurgia ricostruttiva e protesica**")
    st.caption("tecniche mini invasive per la ricostruzione articolare con protocolli fast track")

st.divider()

# --- CONTATTI E PRENOTAZIONI ---
st.header("📅 Contatti e Appuntamenti")
st.write("Per richiedere un consulto o prenotare una visita, compilare il modulo sottostante:")

with st.form("contatti"):
    nome = st.text_input("Nome e Cognome")
    email = st.text_input("Indirizzo Email")
    messaggio = st.text_area("Motivo della visita o richiesta informazioni")
    submit = st.form_submit_button("Invia Richiesta")
    
    if submit:
        st.success("Messaggio inviato correttamente. Il Dr. Franco risponderà al più presto.")

# --- FOOTER OBBLIGATORIO PER MEDICI ---
st.markdown("---")
st.caption("Dr. Domenico Franco - P. IVA: [000000000] | Iscrizione Ordine dei Medici: [00000]")
