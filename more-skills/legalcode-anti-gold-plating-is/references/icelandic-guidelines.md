# Icelandic Guidelines and Deliverable Standards

## Output Language — Read This First

**The report is written entirely in professional, legal Icelandic.** The skill instructions in this file (SKILL.md) are in English; the deliverable is not.

Rules for the deliverable:

1. **No word-for-word translation from English.** Generate Icelandic legal text natively. If a sentence reads like a literal translation ("með beinum sótt af", "ber þungun gegn", "stefnumótunarlegur rökstuðningur"), rewrite it as a native Icelandic speaker would phrase it.
2. **Only foreign primary sources stay in their original language** — verbatim quotations from GDPR articles, EU directive recitals, CJEU/ECJ judgments, and the names of foreign acts (Personopplysningsloven, Databeskyttelsesloven, Tietosuojalaki, Dataskyddslag). Everything else — section headings, classifications, analysis, recommendations, limitations — is in Icelandic.
3. **Use Icelandic legal vocabulary, not calques.** Examples: *svigrúm aðildarríkja* (not "valdrúm"), *ófjárhagslegt tjón* (not "ósnertanlegt tjón"), *tilgreint í greinargerð* (not "tilkynnt"), *vegur þyngra* (not "ber þungun"), *27. liður formála* (not "inngangsorð 27"), *sóttar beint af vef Alþingis* (not "með beinum sótt af althingi.is").
4. **The Icelandic grammar / language pass (Stage 9e) is the last markdown-editing step.** Substantive content is frozen by the verifier pass at 9d. After 9e, the only remaining step is rendering to `.docx` — no further content changes. See Stage 9 below.

## Stage 9e — Report Language and Grammar Pass

**9e — Icelandic language / grammar pass (mandatory; last markdown-editing step).** Read the draft section by section, top to bottom, and rewrite any of the following in native Icelandic legal prose. This is the polish step: substantive content is now frozen; only prose, vocabulary, and grammar change.

- Word-for-word translations from English (calques such as "með beinum sótt", "ber þungun gegn", "stefnumótunarlegur rökstuðningur", "ósnertanlegt tjón", "tilkynnt í greinargerð" where the proper term is "tilgreint", "engin sérstök andmæli fundust" where "engar sérstakar athugasemdir" is natural, "Stutt samantekt í þremur setningum" where "Niðurstaða í þremur setningum" reads cleanly).
- Stilted Anglo-style sentence order; rewrite for Icelandic verb position and natural flow.
- Technical Anglicisms when an established Icelandic legal term exists (e.g., *svigrúm aðildarríkja* not "valdrúm"; *27. liður formála* not "inngangsorð 27"; *vegur þyngra* not "ber þungun gegn"; *ófjárhagslegt tjón* not "ósnertanlegt tjón"; *sóttar beint af vef Alþingis* not "með beinum sótt af althingi.is").
- Capitalised English-style classification labels in headings (translate `Severity: HIGH` to `Alvarleikastig: Há`; `Confidence: Probable` to `Öryggi: Líklegt`; `Pre-law forensics` to `Lagaferill málsins`; `Counter-argument stress test` to `Mótrökspróf`).
- Icelandic morphological correctness — beygingar (declensions and conjugations) of names and technical terms; check that *sbr.* / *skv.* abbreviations are used consistently; check *þ.e.* / *þ.m.t.* spacing.
- **Internal tooling and process references — strip every one.** The deliverable is a standalone legal document for lawyers, Alþingi committees, and regulated parties. It must not mention MCP tool names (`legalcode_search`, `legalcode_trace`, `legalcode_fetch`, `legalcode_analyze`, `cases_for_law`, `pre_law_for_law`, `resultLevel`, `flowKey`, `sourceRef`, `downloadUrl`), skill names (`legalcode-anti-gold-plating-is`, `anti-gold-plating-is`, `Legalcode`, `Anthropic`), internal stage references (`Stage 1`, `Stage 8`, `§8 of the skill`, `Iron Law 7`, `verkferli`, `samkvæmt verkferli`), agent terms (`agent`, `orchestrator`, `subagent`, `tool call`), or working-directory file names (`sources/`, `articles/`, `forensics/`, `stress/`, `revisions/`, `article-index.json`, `frumvarp-mapping.md`). The reader needs the legal substance — not how it was produced. Refer to evidence by its **public citation** (þingskjal number, ákvörðun, dómsmál, umsögn submitter + date) and to method-level requirements (e.g. counter-argument analysis) **without naming the internal procedure or its file**.

#### 9e.1 — Common Icelandic grammar and word-choice errors (general reference)

These patterns appear in any Icelandic prose written by an English-native author and are not law-specific. They were observed empirically in pre-9e drafts of this skill's deliverables and form the core checklist for the 9e pass. Sweep for each category.

**(a) Calques from English — direct word-for-word translations.** These look superficially Icelandic but read as foreign-mind constructions:

| Calque | Standard Icelandic | Why the calque fails |
|---|---|---|
| *„innihalda"* (contain) | *„geyma"*, *„að finna sé í"*, *„hafa að geyma"* | `Innihalda` is for physical/chemical containment; documents *„geyma ákvæði"*. |
| *„beitt eins og skrifað"* (applied as written) | *„beitt eftir orðanna hljóðan"*, *„beitt orðrétt"* | The verb `beinast` does not mean `apply`. |
| *„bera þungan af [áhrifum]"* (bear the brunt of) | *„hafa mest áhrif á"*, *„bera þyngd af"* | English idiom does not map directly. |
| *„teoretísk"* (theoretical) | *„fræðileg"* | Direct adoption of the English word. |
| *„forensik-"* (forensic) | *„rannsóknar-"* | Not a word in Icelandic. |
| *„verbatim"* (Latinism via English) | *„orðréttur"* | |
| *„sectoral"* (English in IS text) | *„sérgreindur"*, *„sérgreint"* | |
| *„rauntækur"* (effective / real-world) | *„raunverulegur"* | The Anglicism reads stilted. |
| *„vernda gegn"* (protect against [something]) | *„vernda [andlag]"* (sögnin tekur þolfall) | The IS verb is transitive: *„verndar persónuupplýsingar"*, not *„verndar gegn brotum"*. |
| *„draga til baka [ákvæði]"* (roll back) | *„fella úr gildi"*, *„nema úr gildi"* | `Draga til baka` is for withdrawing a statement/offer, not legislation. |
| *„starfa undir"* (operate under) | *„starfa eftir"*, *„lúta"* | IS preposition for compliance is `eftir`. |
| *„bjóða upp á"* (provide / offer) | *„veita"* | Colloquial; in formal prose use `veita`. |
| *„léttara skilyrði"* (lighter condition) | *„vægara skilyrði"* | `Léttur` is physical weight; for thresholds use `vægur`. |
| *„sterkasta breyting"* (strongest change) | *„veigamesta breyting"* | `Sterkur` is physical strength; for significance use `veigamikill`. |
| *„hélt [X] óbreyttri"* (kept it unchanged) | *„lét [X] standa óbreytt"* | English `keep` construction is unidiomatic. |
| *„byggði [úrskurð] á"* (based on) | *„reisti [úrskurð] á"* | `Reisa á` is the legal idiom; `byggja á` is acceptable but less formal. |
| *„hægir á"* used for "reduces" | *„dregur úr"* | `Hægja á` literally means slow down. |
| *„draga saman [byrði]"* (intended as reduce) | *„draga úr [byrði]"* | `Draga saman` means summarise/contract; `draga úr` means reduce. |
| *„tilkynntar niðurstöður"* (reported findings) | *„niðurstöður"* | Participle is redundant — judgments are not "announced findings". |
| *„hámarksviðmið samræmingar"* (max harmonisation) | *„hámarkssamræming"*; in tables *„ófrávíkjanlegt"* | Established legal term. |
| *„flækja"* (complicate) | *„torvelda"* | `Flækja` is talmál; `torvelda` is formal. |
| *„skapa hegðun"* (create behaviour) | *„leiða af sér hegðun"*, *„valda hegðun"* | One does not "create" behaviour in IS. |
| *„opna heimild víðar"* (open more widely) | *„rýmka heimildina"* | Standard verb is `rýmka`. |
| *„yrði til hindrunar"* (would be a hindrance) | *„stendur í vegi"*, *„verður hindrun"* | The IS idiom for an obstacle is `standa í vegi`. |
| *„mótbárur"* (objections, formal) | *„athugasemdir"* | `Mótbárur` is talmál; formal IS is `athugasemdir`. |
| *„textaleg afmörkun"* (textual limitation) | *„þrenging"* | The IS legal noun for narrowing is `þrenging`. |
| *„engin sérstök andmæli fundust"* | *„engar sérstakar athugasemdir komu fram"* | Calque of "no specific objections were found". |
| *„textaleg afmörkun frá ófrávíkjanlegri grein"* | *„þrenging á ófrávíkjanlegu ákvæði"* | The IS legal idiom takes `á` + dative. |

**(b) Verb-government and preposition errors (sögn- og forsetningarstýring).** Icelandic verbs and adjectives govern specific cases and prepositions; English-native writers often default to wrong constructions:

- *„vara við að [setning]"* → *„vara við því að [setning]"* — the verb takes a dative pronoun anchor before the `að`-clause.
- *„háð að [grein]"* → *„lýtur skilyrðum [greinar]"* — the adjective `háður` takes dative directly (`háð því`), never `að`. For "subject to [a rule]" the standard verb is `lúta` + dative.
- *„rökstuðningur frávika"* (ef.) → *„rökstuðningur fyrir frávikum"* (þgf.) — IS `rökstuðningur` takes `fyrir` + dative; English `justification of` is a calque.
- *„létta [þf.]"* → *„létta [þgf.]"* — the verb `létta` takes dative: *„léttir formkröfum"*, *„léttir lögfræðilegri óvissu"*.
- *„kæruferli til lögreglu"* → *„kæruferli gagnvart lögreglu"* — the IS preposition for the relational party is `gagnvart`.
- *„fyrir hverja tegund"* (after `rýmkar`) → *„til hverrar tegundar"* — the verb `rýmka til` governs genitive.

**(c) Gender and case agreement (kynjasamræmi og fallaskipting).** The most frequent grammatical errors are agreement mismatches between noun and modifier:

- *„Engar sakamál"* → *„Engin sakamál"* — `sakamál` is hk. ft.; quantifier must be `engin`, not `engar` (kvk. ft.).
- *„fjölmargar úrskurðir"* → *„fjölmargir úrskurðir"* — `úrskurður` is kk.; ft. modifier is `fjölmargir`, not `fjölmargar` (kvk. ft.).
- *„fjárhagslega tjón"* (in nominative) → *„fjárhagslegt tjón"* — `tjón` is hk. nf.; nf. and þf. of the adjective are identical (`fjárhagslegt`); the form `fjárhagslega` is the lh.-mynd / atviksm., which is wrong in nominal contexts.
- *„verulegan áhrif"* → *„veruleg áhrif"* — `áhrif` is hk. ft.; modifier is `veruleg`, not the kk. þf. et. `verulegan`.
- *„almenn stjórnsýsluúrræði"* (when modifying noun adverbially) → *„almennt stjórnsýsluúrræði"* — when "in general / as a rule", use the atviksm. `almennt`, not the lo. `almenn`.
- *„ófrávíkjandi"* → *„ófrávíkjanleg"* — the lh.-nt. form `ófrávíkjandi` (present participle of `víkja`) is not the same as the adjective `ófrávíkjanleg` (-leg-suffixed). Use the latter for the legislative-technique concept.
- *„lögfræðileg óvissu"* → *„lögfræðilegri óvissu"* — `óvissa` is kvk.; dative is `óvissu` with adjective `lögfræðilegri` (kvk. þgf.).

**(d) Verb conjugation, mood, and tense (sagnbeyging, háttur og tíð).**

- After *„í ljósi þess að"* (in light of the fact that), IS legal prose prefers viðtengingarháttur: *„í ljósi þess að engin önnur ríki haldi …"*, not *„halda"*.
- Wrong viðtengingarháttur where nútíð fits: *„þegar greinin yrði til hindrunar"* (viðth. of `yrði`) where the meaning is recurring/general — should be nútíð *„þegar greinin stendur í vegi"*.
- Plural subject demands plural verb: *„verndarráðstafanir helst óbreyttar"* → *„verndarráðstafanir haldast óbreyttar"* (the form `helst` is 3sg of `haldast`).
- *„afnumur"* is not an Icelandic word; the present indicative of `afnema` is `afnemur`.
- Singular noun with plural-implying verb: *„Þvingunarsekt er almenn stjórnsýsluúrræði"* — number must agree. Use ft.: *„Þvingunarsektir eru almennt stjórnsýsluúrræði"*.

**(e) Compound-word formation (samsett orð).** Icelandic compounds use linking morphemes (bandstafir) that English natives often get wrong:

- *„breytingafrumvarp"* → *„breytingarfrumvarp"* — `breyting` requires `-ar-` in compounds; sbr. `breytingartillaga`, `breytingarlög`.
- *„stjórnsýslusektarakerfi"* → *„stjórnsýslusektakerfi"* — use ft. ef. `-sekta-` once, not `-sektar-a-`.
- *„bótabyrð"* → *„bótabyrði"* — the noun is kvk. i-stem `bótabyrði`.
- *„viðurlagaramur"* → *„viðurlagarammi"* — the masculine word for `frame/scope` is `rammi` (weak), not `*ramur`.
- *„Útgáfutímabilstexti"* — not a word; for a release-date metadata field use *„Útgáfudagur"*.
- *„byrgjum"* (intended as `pillars`) — `byrgi` does not carry this metaphor in Icelandic; use *„þættir"* or *„ákvæði"*.

**(f) Double definiteness (tvöföld ákveðni).** Icelandic does not double-mark definiteness: a demonstrative pronoun already conveys it.

- *„sú heimildin"* → *„sú heimild"* — drop the suffixed article when `sú/sá/það` precedes.
- *„þessi maðurinn"* → *„þessi maður"*.

**(g) Concessive conjunctions (`þrátt fyrir að` vs `þótt`).** Two near-synonyms with different register:

- *„þrátt fyrir að"* is heavy/concessive and often a calque from English `despite the fact that`. Best reserved for emphasis on contradiction.
- *„þótt"* is the lighter, more natural Icelandic concessive: *„þótt 15. gr. sé ekki tekin fyrir"*. In legal prose `þótt` reads cleanly; `þrátt fyrir að` is verbose.

**(h) Numerals (talnaritun).** Lágar tölur (≤ 12) eru ritaðar í bókstöfum í lögfræðiprósu: *„á sjö árum"*, ekki *„í 7 árum"*. *„Í 7 árum"* er auk þess enskumengun („in 7 years"); rétta forsetningin er *„á sjö árum"* eða *„á þeim sjö árum sem"* (þolfall án `í`).

**(i) `Tilteknir` vs `ákveðnir` (specific).** *„ákveðnum samningum"* er calque af enska *„certain agreements"*. Á íslensku merkir *„ákveðinn"* (1) ákvarðaður og (2) ákveðinn í afstöðu — ekki *„some unspecified"*. Rétta orðið er *„tiltekinn"*: *„tilteknum samningum"*.

**(j) Ellipsis-pattern from English (`X does, Y does not`).** *„Svíþjóð hefur sambærilegt kerfi, Noregur og Danmörk ekki"* — enskt mynstur `do not`-ellipsis. Á íslensku þarf að klára sögnina: *„Noregur og Danmörk hafa það ekki"*. Auk þess hentar semikomma frekar en komma þegar tvær aðskildar staðhæfingar liggja saman.

**(k) Eignarfall samsvörun í eldri-vísi tilvitnunum.** Þegar tilvísun fer fram með *„(eldri lög nr. X/Y)"* eftir nafnorði í eignarfalli skal `lög` einnig vera í eignarfalli — *„áhrif eldri löggjafar (laga nr. 77/2000)"* en ekki *„(lög nr. 77/2000)"*.

**(l) `vara við [þgf.]` + `því að`** og önnur föst orðasambönd: *„vara við að"* + setning → *„vara við því að"* + setning. Sambærilegt: *„benda á það að"*, *„vekja athygli á því að"*.

**Pre-9f sweep grep — append to existing line 817 sweep:**

```bash
grep -nE "innihalda|teoretís|forensik|verbatim|sectoral|rauntæk|vernda gegn|draga til baka|starfa undir|bjóða upp á|léttara skilyrði|sterkasta breyting|hélt .* óbreyttri|byggði .* á|hægir á|draga saman .* byrð|tilkynntar niðurstöður|hámarksviðmið|\\bflækir\\b|skapa hegðun|opna heimild víðar|yrði til hindrunar|mótbárur|textaleg afmörkun|engin sérstök andmæli|sú [a-zíáéðýúóöþæ]+inn\\b|í [0-9]+ árum|vara við að|háð að|rökstuðningur [a-zíáéðýúóöþæ]+a frá|fyrir hverja tegund|kæruferli til|Engar sakamál|fjölmargar úrskurðir|verulegan áhrif|almenn stjórnsýsluúrræði|\\bófrávíkjandi\\b|lögfræðileg óvissu|breytingafrumvarp|stjórnsýslusektaraker|bótabyrð\\b|viðurlagaramur|byrgjum|ákveðnum samningum|þrátt fyrir að" Gullhudunarskyrsla-*.md Frumvarp-*.md
```

Each hit is a candidate for the table above. Not every hit is wrong (the context matters — `þrátt fyrir að` is sometimes the right concessive), but every hit deserves a moment of review. After resolving hits, the grep returns empty or only the deliberately-kept variants.

**What stays in the source language**, untouched:

- Verbatim quotations from GDPR articles, EU directive recitals, and CJEU/ECJ judgments (English).
- Names of foreign acts (Personopplysningsloven, Databeskyttelsesloven, Tietosuojalaki, Dataskyddslag, Brottsdatalag).
- Names of foreign institutions in their canonical form (Folketinget, Storting, Bundestag, grundlagsutskottet).
- Case identifiers (C-300/21 *Österreichische Post*, E-16/11 *Icesave*).

Sweep with `grep -nE "með beinum|ber þungun|stefnumótunarlegur|ósnertanlegt|frásagnarform|upprunaaktor|tilkynnt í greinargerð|stakeholder|forsöguslóð|valdrúm"` to catch the most common residue from earlier drafts.

**Internal-tooling sweep (mandatory before docx).** Any of these tokens appearing in the deliverable is a hard fail — strip them all:

```bash
grep -nE "legalcode_(search|trace|fetch|analyze|discover)|legalcode-(anti-gold-plating-is|search-agent|agent-pack|counsel|full-bench|adversarial|review|verification|roundtable|tabulate)|anthropic-skills|cases_for_law|pre_law_for_law|laws_for_case|resultLevel|flowKey|sourceRef|downloadUrl|nextAction|Stage [0-9]|§[0-9] (of|í) (the )?skill|verkferli|Iron Law|orchestrator|subagent|tool call|MCP|article-index\.json|frumvarp-mapping\.md|articles/|forensics/|stress/|revisions/|sources/" Gullhudunarskyrsla-*.md
```

Returns must be empty. Replace each hit with the public citation or substantive description it stands in for. Examples:

- `samkvæmt verkferli legalcode-anti-gold-plating-is §8` → delete entirely; the reader needs the *finding*, not the procedure that produced it.
- `úrtak úr legalcode_trace cases_for_law` → `úrtak úr dómaframkvæmd Persónuverndar, Landsréttar og Hæstaréttar` (or list the case numbers directly).
- `Iron Law 7 mótrökspróf` → `mótrökspróf gegn niðurstöðunni` (the method is named, the internal label is not).
- `sbr. sourceRef pre_law_document/IS/...` → cite by þskj. + dagsetning + sender instead.

**After 9e the markdown file is final.** Do not edit the markdown after this step except to fix a typo a Stage 9f docx-rendering check uncovers.

## Stage 10e — Frumvarp Language and Grammar Pass

**10e — Icelandic language / grammar pass (mandatory; last markdown step).** Same discipline as Stage 9e, with three frumvarp-specific additions:

- **Standard amendment-text formulations** — exact phrasings from `references/frumvarp-structure.md` §3.2. Replace any paraphrase with the canonical form (`X. gr. laganna fellur brott.` not "X. gr. is repealed").
- **Quotation marks** — Icelandic low-9 / high-9 (`„texti"`), not Anglo curly (`"texti"`). Sweep: `grep -nE '"[^"]*"' Frumvarp-*.md` and replace each pair with `„`…`"`.
- **Icelandic abbreviations** — `sbr.`, `skv.`, `þ.e.`, `þ.m.t.`, `o.s.frv.` only. No `i.e.`, `e.g.`, `etc.`, `cf.`. Sweep: `grep -nE "\\b(i\\.e\\.|e\\.g\\.|etc\\.|cf\\.)\\b" Frumvarp-*.md` returns nothing.
- **Internal-tooling sweep (mandatory).** Same discipline as Stage 9e. Run the full Stage-9e sweep regex against `Frumvarp-*.md` — must return zero hits. A frumvarp introduced to Alþingi that mentions tool names, skill names, MCP, sourceRefs, or working-directory paths is unfit for filing.
