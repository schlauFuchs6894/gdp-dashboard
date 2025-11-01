# app.py
import streamlit as st
import random

st.set_page_config(page_title="Freunde-Spiele", layout="wide")

tab1, tab2 = st.tabs(["🗳️ Umfrage-Spiel", "🧠 Memory-Spiel"])

# -------------------------------
# TAB 1: Umfrage-Spiel
# -------------------------------
with tab1:
    st.title("🎉 Wer wird am ehesten – Umfrage unter Freunden")

    num_candidates = st.number_input("Wie viele Kandidaten gibt es?", min_value=1, max_value=50, step=1)

    st.subheader("👥 Kandidatennamen eingeben")
    candidates = []
    for i in range(num_candidates):
        name = st.text_input(f"Kandidat {i+1}", key=f"candidate_{i}")
        if name.strip():
            candidates.append(name.strip())

    categories = [
        "Wer wird Millionär?", "Wer wird Influencer?", "Wer wird Politiker?",
        "Wer wird Schauspieler?", "Wer wird Sänger?", "Wer wird Wissenschaftler?",
        "Wer wird Sportler?", "Wer wird Künstler?", "Wer wird Koch?",
        "Wer wird Autor?", "Wer wird Gamer?", "Wer wird Tänzer?", "Wer wird Comedian?",
        "Wer wird Designer?", "Wer wird Fotograf?", "Wer gibt am meisten Geld aus", "Wer wird Musiker?", "Wer wird Unternehmer?",
        "Wer wird Lehrer?", "Wer wird Arzt?", "Wer wird Ingenieur?", "Wer wird am schnellsten obdachlos?",
        "Wer wird Pilot?", "Wer wird Architekt?", "Wer wird Journalist?", "Wer wird Programmierer?",
        "Wer wird Mechaniker?", "Wer wird Friseur?", "Wer wird Landwirt?", "Wer wird Feuerwehrmann?",
        "Wer wird Polizist?", "Wer wird Soldat?"
    ]

    if candidates:
        num_voters = st.number_input("Wie viele Personen stimmen ab?", min_value=1, step=1)

        votes = {category: {name: 0 for name in candidates} for category in categories}

        for voter in range(1, num_voters + 1):
            st.header(f"🗳️ Person {voter} stimmt ab")
            for category in categories:
                choice = st.radio(f"{category}", candidates, key=f"{voter}_{category}")
                votes[category][choice] += 1

        if st.button("📊 Auswertung anzeigen"):
            st.header("Ergebnisse")
            for category in categories:
                st.subheader(f"🏆 {category}")
                sorted_votes = sorted(votes[category].items(), key=lambda x: x[1], reverse=True)
                for i, (name, count) in enumerate(sorted_votes[:3], 1):
                    st.write(f"{i}. {name} – {count} Stimme(n)")
    else:
        st.warning("Bitte gib mindestens einen Kandidatennamen ein.")

# -------------------------------
# TAB 2: Memory-Spiel
# -------------------------------
with tab2:
    st.title("🧠 Memory-Spiel")

    # Kartenpaare definieren
    cards = ["🍎", "🍌", "🍇", "🍓", "🍍", "🥝"]
    cards *= 2
    if "cards" not in st.session_state:
        random.shuffle(cards)
        st.session_state.cards = cards
        st.session_state.flipped = [False] * len(cards)
        st.session_state.matched = [False] * len(cards)
        st.session_state.last_click = None

    if st.button("🔄 Memory zurücksetzen"):
        random.shuffle(cards)
        st.session_state.cards = cards
        st.session_state.flipped = [False] * len(cards)
        st.session_state.matched = [False] * len(cards)
        st.session_state.last_click = None

    # Karten anzeigen
    for row in range(0, len(st.session_state.cards), 6):
        cols = st.columns(6)
        for i in range(6):
            idx = row + i
            if idx < len(st.session_state.cards):
                with cols[i]:
                    if st.session_state.matched[idx] or st.session_state.flipped[idx]:
                        st.button(st.session_state.cards[idx], key=f"card_{idx}", disabled=True)
                    else:
                        if st.button("❓", key=f"card_{idx}"):
                            st.session_state.flipped[idx] = True
                            if st.session_state.last_click is None:
                                st.session_state.last_click = idx
                            else:
                                j = st.session_state.last_click
                                if st.session_state.cards[idx] == st.session_state.cards[j]:
                                    st.session_state.matched[idx] = True
                                    st.session_state.matched[j] = True
                                else:
                                    st.warning("Kein Match!")
                                    st.session_state.flipped[idx] = False
                                    st.session_state.flipped[j] = False
                                st.session_state.last_click = None
