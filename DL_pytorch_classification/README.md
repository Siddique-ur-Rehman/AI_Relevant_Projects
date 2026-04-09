# Yeast Protein Localization Prediction

A deep learning project to predict subcellular localization of yeast proteins using PyTorch. The model classifies yeast proteins into 10 different cellular compartments based on their physicochemical properties.

## 📊 Dataset

- **Source**: Yeast Protein Localization Dataset (UCI Machine Learning Repository)
- **Samples**: 1,484 yeast proteins
- **Features**: 8 numerical attributes (sequence characteristics, hydrophobicity, etc.)
- **Target**: 10 subcellular localization classes
- **Train/Test Split**: 80% / 20% (stratified)

### Target Classes
| Code | Location | Description |
|------|----------|-------------|
| CYT | Cytoplasmic | Cytoplasm |
| ERL | Endoplasmic Reticulum | ER membrane |
| EXC | Extracellular | Outside cell |
| ME1 | Membrane-bound | Membrane protein type 1 |
| ME2 | Membrane-bound | Membrane protein type 2 |
| ME3 | Membrane-bound | Membrane protein type 3 |
| MIT | Mitochondrial | Mitochondria |
| NUC | Nuclear | Nucleus |
| POX | Peroxisomal | Peroxisome |
| VAC | Vacuolar | Vacuole |

## 🏗️ Model Architecture

CustomModel(
(model): Sequential(
(0): Linear(in_features=8, out_features=16, bias=True)
(1): ReLU()
(2): Linear(in_features=16, out_features=10, bias=True)
)
)

### Training Progress

| Epoch | Loss | Accuracy |
|-------|------|----------|
| 10 | 1.9258 | 31.93% |
| 20 | 1.5070 | 45.32% |
| 30 | 1.2978 | 54.17% |
| 40 | 1.1774 | 56.28% |
| 50 | 1.1061 | 58.89% |
| 60 | 1.0621 | 59.22% |
| 70 | 1.0360 | 59.90% |
| 80 | 1.0184 | 60.40% |
| 90 | 1.0054 | 61.16% |
| 100 | 0.9942 | 62.09% |

## 📈 Results

- **Training Accuracy**: 62.09%
- **Training Loss**: 0.9942
- **Training Time**: 0.25 seconds for 100 epochs

