
## 🎨 Text-to-Image lyra Model (by @androidbutut)

Model ini digunakan untuk mengubah teks menjadi gambar secara otomatis, cocok untuk keperluan seperti **AI Storybook**, visualisasi narasi, dan kebutuhan kreatif lainnya.

---

### Cara menjalankan model text2img_lyra
```bash

npx create-replicate --model=androidbutut/text2img_lyr4
```

### Penggunaan node.js

```node
const output = await replicate.run(
  "androidbutut/text2img_lyr4:c1126cda97a58ff1f439abaaf2933876a072d8848a2de2ac46db32cd40ae0635",
  {
    input: {}
  }
);

console.log(output);
```

### Penggunaan phyton
```py
output = replicate.run(
    "androidbutut/text2img_lyr4:c1126cda97a58ff1f439abaaf2933876a072d8848a2de2ac46db32cd40ae0635",
    input={}
)
print(output)
```

### 🔮 Contoh Prompt

"Seorang gadis kecil duduk di bawah pohon sakura, dikelilingi cahaya senja"

Akan menghasilkan gambar AI berdasarkan deskripsi tersebut.

---

### 🚀 Cara Pakai (API)

### Endpoint
```http
POST https://api.replicate.com/v1/predictions
```
Headers
```
Authorization: Token YOUR_REPLICATE_API_TOKEN
Content-Type: application/json
```
Body JSON
```
{
  "version": "androidbutut/text2image-lyra",
  "input": {
    "prompt": "Seekor naga putih terbang di atas gunung es"
  }
}
```

---

📦 Teknologi

Model ini menggunakan:
```
Stable Diffusion v1.5

diffusers library dari Hugging Face

torch + CUDA (untuk percepatan GPU)
```

📚 Paper Referensi

```
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- Penulis: Robin Rombach, Andreas Blattmann, dkk.
```
---

🧠 Untuk Pengembang

Struktur file:
```
├── generate.py         # Entrypoint model
├── replicate.yaml      # Konfigurasi Replicate
└── requirements.txt    # Dependensi Python
```

### Push Model
```
cog login
cog push r8.im/<your-username>/<your-model-name>
```

🖼️ Output

Model akan menghasilkan 1 gambar (output.png) yang otomatis diunggah oleh Replicate dan dikembalikan sebagai URL publik.


---

💬 Dukungan

Model ini dibuat untuk digunakan bersama Lyra Storybook.
Silakan forking, remix, atau request fitur tambahan via issue.


---

⚠️ Lisensi

Model ini menggunakan runwayml/stable-diffusion-v1-5 di bawah lisensi CreativeML Open RAIL-M.
Penggunaan untuk konten eksplisit atau ilegal dilarang.


---

> Dibuat dengan ✨ oleh @androidbutut

