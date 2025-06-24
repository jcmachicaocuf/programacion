{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOq0ApRWBSTNyXHi7Izcb24",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jcmachicaocuf/programacion/blob/main/app.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ukinGxVrWLv4"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "\n",
        "# Cargar el dataset\n",
        "df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')\n",
        "\n",
        "st.title(\"Análisis del Dataset Titanic\")\n",
        "\n",
        "# Filtro por edad\n",
        "st.sidebar.header(\"Filtros\")\n",
        "min_age = st.sidebar.slider(\"Edad mínima\", int(df['Age'].min()), int(df['Age'].max()), int(df['Age'].min()))\n",
        "max_age = st.sidebar.slider(\"Edad máxima\", int(df['Age'].min()), int(df['Age'].max()), int(df['Age'].max()))\n",
        "\n",
        "df_filtered_age = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]\n",
        "\n",
        "st.subheader(\"Datos filtrados por edad\")\n",
        "st.write(df_filtered_age)\n",
        "\n",
        "# Selección de columnas\n",
        "st.subheader(\"Selección de columnas y análisis básico\")\n",
        "selected_cols = ['Survived', 'Pclass', 'Sex', 'Age', 'Fare']\n",
        "selected_data = df_filtered_age[selected_cols]\n",
        "\n",
        "st.write(\"Primeras filas de los datos seleccionados:\")\n",
        "st.write(selected_data.head())\n",
        "\n",
        "# Análisis de sobrevivientes\n",
        "st.subheader(\"Análisis de sobrevivientes\")\n",
        "\n",
        "if not selected_data.empty:\n",
        "    avg_age_survived = selected_data[selected_data['Survived'] == 1]['Age'].mean()\n",
        "    st.write(f\"Edad promedio de sobrevivientes (en datos filtrados): {avg_age_survived:.2f}\")\n",
        "\n",
        "    survivors_by_class = selected_data.groupby('Pclass')['Survived'].sum()\n",
        "    st.write(\"Sobrevivientes por clase (en datos filtrados):\")\n",
        "    st.write(survivors_by_class)\n",
        "else:\n",
        "    st.write(\"No hay datos que cumplan con los criterios de filtro.\")\n"
      ]
    }
  ]
}
