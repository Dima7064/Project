def forward(self, x):
    emb = self.emb(x).transpose(1, 2)
    out = F.relu(self.conv(emb)).max(dim=-1).values
    return self.fc(self.dropout(out))
