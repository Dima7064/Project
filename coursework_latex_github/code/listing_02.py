def forward(self, x, styles, parts, hidden=None):
    emb = self.char_emb(x)
    st = self.style_emb(styles).unsqueeze(1)
    pt = self.part_emb(parts).unsqueeze(1)
    st = st.expand(-1, x.size(1), -1)
    pt = pt.expand(-1, x.size(1), -1)
    inp = torch.cat([emb, st, pt], dim=-1)
    out, hidden = self.lstm(inp, hidden)
    return self.head(self.dropout(out)), hidden
