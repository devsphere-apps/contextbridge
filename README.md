# ContextBridge

> Universal AI project migration toolkit.

ContextBridge converts AI assistant exports into portable knowledge bases that can be reused across different AI platforms.

## Vision

Move project knowledge instead of starting over.

Instead of locking conversations inside a single AI platform, ContextBridge transforms them into portable knowledge that can be imported, indexed, and reused anywhere.

## Features

- ✅ Claude export loader
- ✅ Claude conversation parser
- ✅ Claude message parser
- ✅ Project inspection
- ✅ Universal `ProjectContext`
- ✅ Markdown knowledge base export
- ✅ Export all conversations
- ✅ Export a single conversation by UUID
- ✅ Export directly from a Claude conversation URL
- 🚧 Support for additional AI providers

## Installation

```bash
git clone https://github.com/devsphere-apps/contextbridge.git
cd contextbridge

python -m venv .venv
source .venv/bin/activate

pip install -e .
```

## Usage

### Show version

```bash
contextbridge version
```

### Inspect a Claude export

```bash
contextbridge inspect ~/Downloads/claude-export
```

Example output:

```
✓ Claude export detected

Conversations: 230
Messages:      8275
```

### Export all conversations

```bash
contextbridge export \
~/Downloads/claude-export \
--format markdown \
--output exports
```

### Export a single conversation

```bash
contextbridge export \
~/Downloads/claude-export \
--conversation c389aee2-0811-4326-a898-f3871969eaf7
```

### Export directly from a Claude URL

```bash
contextbridge export \
~/Downloads/claude-export \
--url "https://claude.ai/chat/c389aee2-0811-4326-a898-f3871969eaf7"
```

## Roadmap

### v0.1 ✅

- [x] Claude export loader
- [x] Conversation parser
- [x] Message parser
- [x] Project inspection
- [x] Universal `ProjectContext`
- [x] Markdown knowledge base exporter
- [x] Export CLI
- [x] Export by conversation UUID
- [x] Export by Claude conversation URL

### v0.2

- [ ] Improve Markdown knowledge base
- [ ] Export attachments and referenced files
- [ ] Generate `index.md`
- [ ] Better conversation organization

### v0.3

- [ ] Claude memories parser
- [ ] Claude projects parser
- [ ] Universal AI Project Format (UAPF)

### Future

- [ ] Cursor compatibility
- [ ] Gemini compatibility
- [ ] Additional AI providers

## License

MIT