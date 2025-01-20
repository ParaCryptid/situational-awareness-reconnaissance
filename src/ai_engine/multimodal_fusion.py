import numpy as np

class MultimodalFusion:
    def __init__(self):
        self.text_data = []
        self.image_data = []
        self.audio_data = []
        self.video_data = []

    def add_text_data(self, text_embeddings):
        self.text_data.append(text_embeddings)

    def add_image_data(self, image_features):
        self.image_data.append(image_features)

    def add_audio_data(self, audio_features):
        self.audio_data.append(audio_features)

    def add_video_data(self, video_features):
        self.video_data.append(video_features)

    def fuse_data(self):
        # Normalize and concatenate all modalities
        modalities = [self.text_data, self.image_data, self.audio_data, self.video_data]
        fused_data = [np.mean(np.array(mod), axis=0) for mod in modalities if mod]
        return np.concatenate(fused_data, axis=0) if fused_data else None

# Example usage
# fusion_engine = MultimodalFusion()
# fusion_engine.add_text_data([0.2, 0.3, 0.5])
# fusion_engine.add_image_data([0.1, 0.4, 0.5])
# result = fusion_engine.fuse_data()
# print("Fused Data:", result)
